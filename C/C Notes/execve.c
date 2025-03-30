/****************************************************************************************************************************************************************************************************************************************************************/
// Notes for execve() function in C.
// -> ¿Para qué sirve la función execve()?
//         Sirve para crear un proceso diferente al actual.
// -> ¿Qué recibe o devuelve la función?
//         La función devuelve un 0 si no falla, y un -1 si falla. Recibe el nuevo proceso a realizar, todos los argumentos necesarios (empezando por el proceso y terminando por NULL), y por último recibe un contexto, que en su mayoría pondremos NULL.
// -> ¿Le puedo pasar todo lo que necesita recibir la función directamente?
//         No, es mejor crear una lista, y pasarle primero el primer elemento de la lista como primer argumento, y toda la lista entera como segundo argumento. Como tercer y último argumento, le pasaremos NULL directamente.
/****************************************************************************************************************************************************************************************************************************************************************/
// Ejemplo de función execve()

#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int main( char argc, char* argv[]){

  char * myargv[] = { "/bin/directorio_inexistente/ls", "-l", NULL};
  char * myenv[] = { NULL};

  if( execve( myargv[ 0], myargv, myenv) == -1){    
    perror( "Error lanzando el programa de ejemplo.");     
    exit( -1);
  }

  printf("Boo!!\n");

  return 0;
}