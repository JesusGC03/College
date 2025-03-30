#############################################################################################
# Resumen de las Estructuras de Datos en Python                                             #
# Veremos los usos, métodos y aplicaciones.                                                 #
# Son herramientas esenciales para organizar y almacenar informacion eficientemente         #
#############################################################################################


# Tipos de Estructuras #

    #1- LISTAS
    #Colección ordenada y mutable de elementos.
    #Métodos comunes: append(), insert(), remove(), pop(), sort().

amigos = ['Mery', 'Richi', 'Mikel']
amigos.append('Lucas')                  #['Mery', 'Richi', 'Mikel', 'Lucas']


    #2- TUPLAS
    #Similar a las listas, pero éstas son inmutables. Son más eficientes en memoria y rendimiento.
    #Soportan indexación, rebanado y desempaquetado.
    #INDEXACIÓN -> Posibilidad de acceder a un elemento por su posición
    #REBANADO -> Permite seleccionar y extraer un subconjunto de elementos de una colección ordenada.
    #DESEMPAQUETADO -> Permite extraer valores de un conjunto para asignarlos a variables

tupla = (1, 2, 3)
print(tupla[0])                          #indexación
a, b, c = tupla                          #desempaquetado
print(a)                                 #1
print(b)                                 #2
print(tupla[1:2])                        #rebanado -> (2,)


    #3- CONJUNTOS (SET)
    #Colección no ordenada de elementos únicos. Soportan unión, intersección y diferencia.
    #Métodos comunes: add(), remove(), union(), intersection()

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.add(4)                          #{1, 2, 3, 4}
set1.remove(2)                       #{1, 3, 4}
set1.update(set2)                    #{1, 3, 4, 5}
intersection = set1 & set2           #{3, 4, 5}


    #4- DICCIONARIOS
    #Colección no ordenada pares clave-valor. Permiten el acceso rápido mediante claves únicas.
    #Métodos comunes: get(), key(), values(), items()

diccionario = {'nombre': 'Ana', 'edad': 30}
diccionario['edad'] += 1                            #{'nombre': 'Ana', 'edad': 31}


    #5- ENUMERACIONES
    #Conjunto de nombres simbólicos asociados a valores constantes.
    #Mejora la legibilidad del código y evita el uso de "números mágicos"

from enum import Enum

class EstadoTarea(Enum):
    PENDIENTE = 1
    EN_PROGRESO = 2

print(EstadoTarea.PENDIENTE.name)        #'PENDIENTE'


    #6- ARRAYS (NumPy)
    #Más rápidos y eficientes que las listas para las operaciones matemáticas.
    #Soportan múltiples dimensiones

import numpy as np

arreglo = np.array([1, 2, 3])
arreglo[1] = 10                          #[1, 10, 3]




# Operaciones Especiales #

    #1- LISTAS COMO PILAS
    #Operaciones comunes: push(Añadir), pop(Eliminar y devolver el último)

pila = []
pila.append(1)
pila.append(2)
print(pila.pop())                        #2


    #2- LISTAS COMO COLAS
    #Utilizan el módulo "deque" para mayor eficiencia.
    #Operaciones comunes: append(Añadir al final), popleft(Eliminar del inicio)

from collections import deque

cola = deque()
cola.append('A')
print(cola.popleft())                    #'A'


    #3- OPERACIONES CON DICCIONARIOS
    #Iterar claves, valores, o pares clave-valor.

for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")
