/*******************************************************************************************************************************************************************************************/
// Notes for fork() function in C. Also see function getpid() and getppid()
// -> ¿Para qué sirve la función fork()?
//         Para crear procesos hijos, a partir de un proceso original (padre), utilizamos la funcion fork().
// -> ¿Qué recibe o devuelve la función?
//         La función no recibe nada (NULL), mientras que devuelve la PID del proceso hijo creado.
// -> ¿Cómo se en que proceso estoy, en el hijo o en el padre?
//         Sabemos en cuál proceso estamos mediante una comparación. 
//         Si la PID devuelta por la función es 0, entonces estamos en el proceso padre.
//         Si por el contrario la PID es distinta de 0, entonces estamos en el proceso hijo.
// -> ¿Si estoy en el proceso hijo, como sé su PID y la PID del proceso padre?
//         Si estamos dentro del proceso hijo, para sacar su PID utlizamos la llamada "getpid()", y para sacar la PID del proceso padre, utilizamos "getppid()".
//         Si por el contrario estamos en el proceso padre, la PID del proceso hijo la podemos sacar de lo que devuelve la función fork(), y la PID del padre, con la función "getpid()".
/*******************************************************************************************************************************************************************************************/
// Ejemplo de función fork()

#include <stdio.h>
#include <unistd.h>

int main(int argc, char* argv[]){

    int pid, ppid;

    pid = fork();

    if(pid != 0){

        printf("I'm (%d), my son is (%d).\n", getpid(), pid);

    }else{

        printf("I'm (%d), my father is (%d).\n", getpid(), getppid());

    }

    return 0;

}