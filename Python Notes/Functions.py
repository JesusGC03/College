#############################################################################################
# Resumen de las Funciones en Python                                                        #
# Veremos conceptos básicos y avanzados sobre las funciones de Python                       #
# Incluyendo tipos de funciones, componentes, valores por referencia y valor, anidadas,     #
#       parámetros múltiples, anotaciones, funciones lambda y decoradores.                  #
#############################################################################################


# Introducción a las funciones #

    #1- FUNCIONES BÁSICAS
    #Una función es un código reutilizable que realiza una tarea específica.
    #Pueden ser incorporadas por el mismo lenguaje de python, o definidas por el usuario.

def saludar():
    print("Hola Mundo")

saludar()


    #2- CONVERSIONES DE TIPOS
    #Python convierte automáticamente tipos numéricos en ciertas expresiones.
    #También existe la posibilidad de usar las funciones "int()" o "float()".

print(float(99)/100)
print(int("123")+1)


    #3- PARÁMETROS Y ARGUMENTOS
    #PARÁMETRO -> Variable usada en la definición de la función.
    #ARGUMENTO -> Valor pasado al llamar la función.

def saludar(nombre):                    #Parámetro: nombre = "María"
    print(f"Hola, {nombre}")

saludar("María")                        #Argumento: María


    #4- VALORES RETORNADOS
    #Las funciones tienen la posibilidad de devolver valores con "return".
    #Los "return" nos permiten devolver valores en la misma línea, es decir, realizar las operaciones en la misma línea del return.

def suma(a, b):
    return a + b

print(suma(3, 4))


    #5- MULTIPLES PARÁMETROS Y RETORNOS
    #*ARGS -> Utilizado para pasar múltiples argumentos posicionales.
    #**KWARGS -> Utilizado para argumentos con nombres.

def suma(*numeros):                             #Ejemplo con *args
    return sum(numeros)

print(suma(1, 2, 3, 4))


def mostrar_info(**info):                       #Ejemplo con **kwargs
    for clave, valor in info.items():
        print(f"{clave}, {valor}")

mostrar_info(nombre="Ana", edad=25)


    #6- FUNCIONES ANIDADAS
    #Para mejorar la encapsulación, y ahorrar tiempo y espacio, definimos una función dentro de otra (como los bucles).

def exterior(texto):
    def interior():
        print(texto)
    interior()

exterior("Hola desde el interior")


    #7- FUNCIONES LAMBDA
    #Funciones breves y anónimas, creadas en una sola línea de código.

cuadrado= lambda x: x ** 2
print(cuadrado(5))


    #8- DECORADORES
    #Modifican el comportamiento de funciones o clases sin alterar su código fuente.

def decorador(func):
    def envoltura():                                            
        print("Antes de la función")                            
        func()                                                  #Llama a la función original
        print("Después de la función")                          
    return envoltura

@decorador                                                      #Esto aplica el decorador a la función "saludar()"
def saludo():                                                   #SALIDA
    print("Hola!")                                              #Antes de la función
                                                                #Hola!
saludo()                                                        #Después de la función
