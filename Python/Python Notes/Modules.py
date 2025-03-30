#############################################################################################
# Resumen de Módulos y Paquetes                                                             #
# Los módulos son archivos que contienen definiciones, funciones y clases reutilizables     #
# Los paquetes son carpetas que contienen múltiples módulos organizados.                    #
#############################################################################################


# Módulos #

    #1- ¿QUÉ ES UN MÓDULO?
    #Archivo con funciones reutilizables para organizar mejor el código.


    #2- CREACIÓN DE MÓDULOS
    #Vamos a crear el archivo mimodulo.py y usarlo en otro archivo.

# mimodulo.py #

def suma(a, b):
    return a + b

def resta (a, b):
    return a - b

# main.py #
import mimodulo
print(mimodulo.suma(4, 3))
print(mimodulo.resta(10, 9))


    #3- IMPORTACIÓN DE COMPONENTES ESPECÍFICOS
    #Puedes importar funciones o variables específicas, en vez de importar el archivo entero.

from mimodulo import suma
print(suma(4, 3))


    #4- IMPORTAR TODO
    #Utilizando "*", podemos importar todo el contenido de un archivo.

from mimodulo import *


    #5- MÓDULOS EN CARPETAS
    #Usa el nombre de la carpeta para importar.

from mifolder.hello import HelloWorld
HelloWorld()


    #6- GESTIÓN DE RUTAS DE BÚSQUEDA
    #Python busca módulos en rutas definidas por "sys.path", pudiendo agregar una ruta personalizada.

import sys
sys.path.append('/path/to/your/module')


    #7- RENOMBRAR MÓDULOS
    #Utilizando "as", podemos cambiar el nombre del módulo.

import modulowithlongname as m
m.fun()


    #8- MANEJO DE ERRORES AL IMPORTAR
    #Maneja errores como "ModuleNotFoundError " usando "try" y "except"

try:
    import non_existent_module
except ModuleNotFoundError as e:
    print("Error:", e)


    #9- RECARGAR MÓDULOS
    #Los módulos se cargan solo una vez. Si quieres recargarlos explícitamente

import importlib
importlib.reload(mimodulo)




# Módulos #

    #1- ¿QUÉ ES UN PAQUETE?
    #Carpeta que contiene módulos y un archivo "__init__.py".


    #2- ESTRUCTURA BÁSICA
    
# mypackage/
#     __init__.py
#     module1.py
#     module2.py
#     subpackage/
#         __init__.py
#         module3.py


    #3- IMPORTACIÓN DESDE PAQUETES
    #IMPORTAR EN UN MÓDULO -> from mypackage import module1
    #IMPORTAR DESDE UN SUBPAQUETE -> from mypackage.subpackage import module3


    #4- SINTAXIS DE IMPORTACIÓN

import paquete.modulo
from paquete import modulo
from paquete.modulo import funcion