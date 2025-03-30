/*******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************/
// Notes for threads in C.
// -> ¿Qué son los hilos?
//         Pequeños procesos que realizan una tarea concreta dentro de un proceso mayor. Estos pueden ser múltiples dentro de un programa grande y llevar a cabo varias tareas de manera simultánea, ahorrandonos mucho tiempo de ejecución y procesamiento.
// -> ¿Cómo se crean los hilos?
//         Se crean con la función pthread_create(). Esta llamada crea un nuevo hilo, el cual recibirá: el identificador del nuevo hilo pasado por referencia (almacenado dentro de una estructura), los atributos del nuevo hilo, el punto de inicio del hilo, y los argumentos para la función de inicio.
//         (Realmente, los unicos que nos importan son los parametros del punto de inicio y de los argumentos)
// -> ¿Qué le tengo que pasar por el parámetro de punto de inicio?
//         Una función con este aspecto < void * punto_de_inicio( void * argumento) >, en la que, dentro de la función, se realizará la función que queremos que haga el hilo.
// -> ¿Cómo se finaliza un hilo?
//         Con la llamada pthread_exit(). Esta llamada finaliza un hilo y retorna un valor a través de un parámetro, el cuál, puede ser recuperado por la llamada pthread_join(). También se puede poner NULL si no se quiere retornar un valor.
// -> ¿Como podemos esperar a que finalice un hilo?
//         Con la llamada pthread_join(). Esta llamada hace que el proceso espera a que finalice el hilo deseado, salvo que ya haya finalizado. Puede recuperar en una variable el valor devuelto en la llamada pthread_join().
// -> ¿Como protegemos datos compartidos y solucionamos las condiciones de carrera?
//         Con la llamada pthread_mutex_init(), inicializamos un mutex a una variable para bloquearla o desbloquearla y poder proteger sus valores. Recibe una variable de tipo estructura pthread_mutex_t pasada por referencia, y los atributos del mutex (En nuestro caso, mayoritariamente será NULL).
// -> ¿Cómo bloqueamos y desbloqueamos la variable?
//         Con las llamadas pthread_mutex_lock() y la llamada pthread_mutex_unlock(). Para poder bloquear y proteger la variable, utilizamos la llamada pthread_mutex_lock(), pasandole la referencia de la variable que queremos bloquear. Para desbloquearla, utilizamos pthread_mutex_unlock(), recibiendo también la referencia de la variable a desbloquear.
/*******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************/
// Ejemplo de creación de hilos.

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

void * thread_func( void * arg){

  char * msg = (char *) arg;

  while( 1){ 
    usleep( rand() % 3000000);
    puts( msg);
  }
}

int main( int argc, char* argv[]){

  pthread_t th1, th2, th3;

  pthread_create( &th1, NULL, thread_func, "Hello!");
  pthread_create( &th2, NULL, thread_func, "Hola!");
  pthread_create( &th3, NULL, thread_func, "Namaste!");

  sleep( 10);
  
  return 0;
}

// Ejemplo de creación de hilos 2

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>

struct thread_data{
    int nrep;
    char msg[10];
};


void * thread_func( void * arg){

  struct thread_data *data = (struct thread_data *)arg; // Como arg es un puntero a thread_data, que es el argumento pasado en el programa main, hay que tratarlo como la estructura.
  // char * msg = (char *) arg;
  int i = 0;

  while( i < data->nrep){ 
    usleep( rand() % 3000000);
    printf("(%02d) %d %s\n", i, data->nrep, data->msg);
    i++;
  }
  pthread_exit( NULL);
}

int main( int argc, char* argv[]){

  pthread_t th1, th2, th3;
  
  struct thread_data thd1, thd2, thd3;

  thd1.nrep = 5;
  strcpy(thd1.msg, "Hello!");
  thd2.nrep = 3;
  strcpy(thd2.msg, "Hola!");
  thd3.nrep = 4;
  strcpy(thd3.msg, "Namaste!");

  pthread_create( &th1, NULL, thread_func, &thd1);
  pthread_create( &th2, NULL, thread_func, &thd2);
  pthread_create( &th3, NULL, thread_func, &thd3);

  pthread_join( th1, NULL);
  pthread_join( th2, NULL);
  pthread_join( th3, NULL);
  
  return 0;
}

// Ejemplo de bloqueo y desbloqueo de variables

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

#define TOTAL_COUNT 400000000

long x = 0;
pthread_mutex_t lock; // Creamos variable global

void * thread_func( void * arg){

  long count = *(long *)arg;
  long local = 0; // Creamos una variable local para registrar los aumentos.

  for( long i = 0; i < count; i++){
	  local++;
  }

  // Hacemos el bloqueo y desbloqueo una sola vez para evitar que esté haciendolo en cada iteración.
  pthread_mutex_lock(&lock); // Bloqueamos la variable
  x=local;
  pthread_mutex_unlock(&lock); // La desbloqueamos
}

int main( int argc, char* argv[]){

  long total_count = TOTAL_COUNT;
  int nthreads;

  if( argc == 1)
    nthreads = 1;
  else
    nthreads = atoi( argv[1]);

  pthread_t th[nthreads];
  long th_count[nthreads];

  pthread_mutex_init(&lock, NULL); // Iniciamos el lock

  for( int i = 0; i < nthreads; i++){
    th_count[i] = total_count/(nthreads-i);
    pthread_create( &th[i], NULL, thread_func, &th_count[i]);
    total_count -= th_count[i];
  }

  for( int i = 0; i < nthreads; i++)
    pthread_join( th[i], NULL);

  pthread_mutex_destroy(&lock); // Quitamos el lock

  printf("%ld\n", x);

  return 0;

}