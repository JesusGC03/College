/*******************************************************************************************************************************************************************************************************************************/
// Notes for wait() / waitpid() function in C. Also see function WEXITSTATUS() and WIFEXITED().
// -> ¿Para qué sirve la función wait()?
//         Sirve para hacer que el proceso padre espere a que finalice alguno de los procesos hijos.
// -> ¿Qué recibe o devuelve la función?
//         La función puede recibir una variable para guardar el estado de salida del proceso hijo ó nada (NULL), y devuelve la PID del proceso.
// -> ¿Para qué sirve la función waitpid()?
//         Sirve para hacer que el proceso padre espere a que un proceso hijo finalice.
// -> ¿Qué recibe o devuelve la función?
//         La función recibe la PID del proceso que tiene que esperar a que finalice, una variable para guardar el estado de salida del proceso (o NULL en su defecto), y un contexto de finaliazción (0 por ahora)
// -> ¿Como sé si ha finalizado realmente el proceso?
//         La función WIFEXITED(status), devuelve TRUE o FALSE dependiendo de si el estado de salida del proceso guardado en la variable status ha finalizado o no.
// -> ¿Cómo sé con qué estado de salida ha finalizado el proceso?
//         La función WEXITSTATUS(status), nos devuelve el estado de salida del proceso que ha finalizado.
/*******************************************************************************************************************************************************************************************************************************/
// Ejemplo de función wait()

#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

int main( int argc, char* argv[]){

    if( fork() != 0){ 
        printf("Padre: esperando a que finalice el proceso hijo...\n");
	int pid = wait(NULL);
        printf("Padre: hijo (%d) finalizado.\n", pid);
    } else {
        printf("Hijo: durmiendo unos segundos...\n");
        sleep( 1); 
        printf("Hijo: finalizando.\n");
    }   

    return 0;
}

// Ejemplo de funcion waitpid()

#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

int main( int argc, char* argv[]){

    pid_t pid1, pid2;
    
    if( (pid1=fork()) != 0){ 

        if( (pid2=fork()) != 0){ 

            printf("Padre: esperando a que acabe el Hijo 1...\n");
	        waitpid(pid1, NULL, 0);
            printf("Padre: Hijo 1 finalizado. Esperando a que acabe el Hijo 2...\n");
	        waitpid(pid2, NULL, 0);
            printf("Padre: Hijo 2 finalizado. THE END.\n");

        }else{

            printf("Hijo 2: durmiendo unos segundos...\n");
            sleep( 2); 
            printf("Hijo 2: despertado y finalizando.\n");

        }   

    }else{

        printf("Hijo 1: durmiendo unos segundos...\n");
        sleep( 3); 
        printf("Hijo 1: despertado y finalizando.\n");

    }   

    return 0;

}

// Ejemplo de WEXITSTATUS()

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>

int main( int argc, char* argv[]){

	int pid, ext;

    if( fork() != 0){

        printf("Padre: esperando a que finalice el proceso hijo...\n");
	    pid = wait(&ext);
        printf("Padre: hijo (%d) finalizado con estado de salida %d.\n", pid, WEXITSTATUS(ext));

    } else {

        printf("Hijo: durmiendo unos segundos...\n");
        sleep( 1);
        printf("Hijo: finalizando.\n");
        exit(1);

    }

    return 0;

}   

// Ejemplo de WIFEXITED()

