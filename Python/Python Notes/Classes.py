#############################################################################################
# Resumen de las clases en Python                                                           #
# Veremos los conceptos fundamentales, y su implementación en código                        #
#############################################################################################

# Clases e Instancias #

    #1- CLASES E INSTANCIAS
    #CLASE -> Tipo de dato que agrupa atributos y métodos
    #INSTANCIA -> Objetos individuales creados a partir de una clase.

class Persona:                  #Esto es una clase
    pass

persona = Persona()             #Y esto una instancia


    #2- INICIALIZADOR
    #Método especial que inicializa atributos de un objeto.
    #Se invoca al crear una instancia.

    #3- SELF
    #Hace una referencia al objeto actual. Permite acceder a atributos y métodos de un objeto.

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


    #4- CONTROL DE ACCESO
    #Hay tres niveles de acceso: público, protegido y privado
    #PÚBLICO -> Sin prefijo especial. Accesibles desde cualquier lugar.
    #PROTEGIDO -> Comienzan con un guión bajo. Accesibles en subclases.
    #PRIVADO -> Comienzan con un doble guión bajo. Utilizan "name mangling" para evitar colisiones de nombres.

class Ejemplo:
    def __init__(self):
        self.publico
        self._protegido
        self.__privado


    #5- ATRIBUTOS
    #Hay dos tipos de atributos: de clase y de instancia.
    #DE CLASE -> Compartidos por todas las instancias.
    #DE INSTANCIA -> Únicos por cada objeto.

class Persona:
    especie = "Homo Sapiens"            #Atributo de clase
    def __init__(self, nombre):
        self.nombre = nombre            #Atributo de instancia


    #6- MÉTODOS ESPECIALES
    #Dos tipos de métodos especiales: de clase y estáticos.
    #DE CLASE -> Utilizan "@classmethod". Acceden a atributos de clase.
    #ESTÁTICOS -> Utilizan "@staticmethod". No acceden a instancia ni a clase.

class Persona:
    @staticmethod
    def es_adulto(edad):
        return edad >=18


    #7- GETTERS Y SETTERS
    #Los métodos getter y setter controlan el acceso y la modificación de un atributo. 
    #Se pueden implementar con "@property"

class Persona:
    def __init__(self, altura):
        self._altura = altura

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, nueva_altura):
        self._altura = nueva_altura


    #8-EJEMPLO COMPLETO

import datetime

class Persona:
    especie = "Homo Sapiens"
    
    def __init__(self, nombre, apellido, nacimiento):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__nacimiento = datetime.datetime.strptime(nacimiento, "%Y-%m-%d")
    
    @property
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"
    
    @nombre_completo.setter
    def nombre_completo(self, nuevo_nombre):
        self.__nombre, self.__apellido = nuevo_nombre.split()
    
    def _calcular_edad(self):
        hoy = datetime.datetime.today()
        return hoy.year - self.__nacimiento.year
    
    @staticmethod
    def es_adulto(edad):
        return edad >= 18
