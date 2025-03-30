/**********************************************************************************************************************************************************************************************************************************************************************************************/
// Notes for signal() and sigaction(). function in C. See also function raise() and how to handle signals in C.
// -> ¿Para qué sirve la función signal()?
//         Sirve para modificar la acción que realiza la señal indicada, mediante una función diseñada manualmente.
// -> ¿Qué recibe la función signal()?
//         Primero, recibe la señal que queremos editar. Segundo, recibe la función diseñada por nosotros para editar la función de la señal (el sighandler).
// -> ¿Para qué sirve la función sigaction()?
//         Tiene la misma función que signal(), pero más compleja ya que en vez de recibir el handler, recibe una acción representada por una estructura previamente diseñada.
// -> ¿Qué recibe la función sigaction()?
//         Primero, recibe la señal que queremos editar. Segundo, recibe la dirección de memoria de la estructura creada previamente mencionada. Tercero, le podemos pasar la antigua acción de la señal designada, por si se desea volver a registrarla después (Nosotros le pasaremos NULL).
// -> ¿Como trataremos el handler para cada función?
//         * Para signal(), usaremos la función < void sighandler(int n) >, siendo "n" la variable con la que diferenciaremos la señal recibida.
//         * Para sigaction(), usaremos la funcion < void mysigaction(int n, siginfo_t * info, void * context) >, donde "n" vuelve a ser la variable para diferenciar la señal recibida, y la estructura "info" la utilizaremos para sacar información adicional de nuestro interés.
// -> ¿Para qué sirve la función raise()?
//         Sirve para realizar una llamada a una señal desde el propio proceso. Es decir, si estamos dentro de un proceso y tenemos un "raise(SIGINT)", cuando el programa llegue a esa parte del código, el propio proceso mandará una señal de interrupción.
/**********************************************************************************************************************************************************************************************************************************************************************************************/
// Ejemplo función signal() y handler para esa función

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

#define START_VAL 100000000

void mysighandler( int n);

int main( int argc, char* argv[]){

    long i, j;

    struct sigaction a;

    a.sa_handler = mysighandler;
    sigemptyset( &a.sa_mask);
    a.sa_flags = 0; // Puede estar entre 0 y 3.

    sigaction( SIGINT, &a, NULL);

    for( i = START_VAL; ; i++){
      for( j = 2 ; j < i; j++)
        if ((i % j) == 0)
          break;
      if( j == i)
        printf("%ld\n", i); 
    }   

    return 0;
}

void mysighandler( int n){

    printf("It is a good day to die... but the day is not yet over.\n");
    signal( SIGINT, SIG_DFL);
}

// Ejemplo función sigaction() y handler para esa función

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

#define START_VAL 100000000

void mysigaction( int n, siginfo_t * info, void * context);

int main( int argc, char* argv[]){

    long i, j;

    struct sigaction a;

    a.sa_sigaction = mysigaction;
    sigemptyset( &a.sa_mask);
    a.sa_flags = SA_SIGINFO;

    sigaction( SIGINT, &a, NULL);

    for( i = START_VAL; ; i++){
      for( j = 2 ; j < i; j++)
        if ((i % j) == 0)
          break;
      if( j == i)
        printf("%ld\n", i); 
    }   

    return 0;
}

void mysigaction( int n, siginfo_t * info, void * context){

    printf("It is a good day to die... but the day is not yet over.\n");
    printf("Signal ID: %d\n", info->si_pid);
    signal( SIGINT, SIG_DFL);
}

// Ejemplo función raise()

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <sys/types.h>
#include <unistd.h>
#include <signal.h>
#include "foominerlib.h"

int tp_c = 0, tout = 0;

void mysigaction(int n, siginfo_t *info, void *context);

int main(int argc, char *argv[]) {
    int difficulty;
    uint32_t nonce_start, nonce_end, nonce_sol;
    struct fooblock b;
    char *blockfile;
    struct sigaction a;

    if (argc < 5) {
        printf("Too few arguments.\nUsage:\n");
        printf("%s <block file> <difficulty> <nonce start> <nonce end>\n", argv[0]);
        return -1;
    }

    a.sa_sigaction = mysigaction;
    sigemptyset(&a.sa_mask);
    a.sa_flags = SA_SIGINFO;
    sigaction(SIGUSR1, &a, NULL);
    sigaction(SIGINT, &a, NULL);
    sigaction(SIGALRM, &a, NULL);

    blockfile = argv[1];
    difficulty = atoi(argv[2]);
    nonce_start = (uint32_t) atol(argv[3]);
    nonce_end = (uint32_t) atol(argv[4]);

    if (fooblock_load(blockfile, &b) == -1)
        return -1;

    if (fooblock_mine(&b, difficulty, nonce_start, nonce_end, &nonce_sol) == 0) {
        printf("(%d) found nonce %u is valid.\n", getpid(), nonce_sol);
        fooblock_save_solved(blockfile, &b, nonce_sol);
        return 0;
    }
    printf("(%d) Nonce not found.\n", getpid());
    return 1;
}

void mysigaction(int n, siginfo_t *info, void *context) {
    if (n == SIGUSR1) {
        printf("Miner (%d) working, %d hashes checked.\n", getpid(), hashes);
    } 
    else if (n == SIGINT) {
        printf("Requesting miner status...\n");
        raise(SIGUSR1);

        if (tp_c == 0) { // Se pulsa por primera vez Ctrl+C.
            tp_c = 1; // Cambiamos las variables de control.
            tout = 0;
            printf("Press Ctrl+C again within 2 seconds to terminate.\n");
            alarm(2); // Inicializamos la alarma en 2 segundos.
        } 
        else if (tout == 0) { // Si no han pasado los dos segundos y se vuelve a pulsar Ctrl+C.
            printf("Termination requested.\n"); // Imprime por pantalla la peticion de finalizar.
            exit(1); // Y finaliza.
        } 
    } 
    else if (n == SIGALRM) { // Si se activa la alarma
        printf("Termination cancelled.\n"); // Se imprime por pantalla que se ha cancelado la finalización.
        tp_c = 0; // Y se reestablecen las variables de control.
        tout = 1;
    }
}