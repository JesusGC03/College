#############################################################################################
# Resumen de la programación orientada a objetos                                            #
# Con sus principios básicos, beneficios, y aplicaciones                                    #
# Beneficios de OOP: Modularidad, Reutilización, Facilidad de Mantenimiento y Pluggabilidad #
#############################################################################################

# Principios Básicos de OOP #

    #1- CLASES Y OBJETOS
    #CLASE -> Una clase es una plantilla para crear objetos con propiedades y métodos.
    #OBJETO -> Un objeto es una instancia de clase

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre;
        self.edad = edad;

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}"

persona=Persona("Juan", 30)
print(persona.saludar())


    #2- ENCAPSULACION
    #Combina datos y métodos en una unidad.
    #Controla el acceso mediante niveles: público, protegido(_) y privado(__)

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def obtener_saldo(self):
        return self.__saldo

cuenta=CuentaBancaria(300)
print(cuenta.obtener_saldo())
cuenta.depositar(50)
print(cuenta.obtener_saldo())


    #3- HERENCIA
    #Permite crear nuevas clases basadas en otras existentes, promoviendo la reutilización
    #Puede ser simple o múltiple.

class Animal:
    def sonido(self):
        pass

class Perro(Animal):
    def sonido(self):
        return "Guau"

class Gato(Animal):
    def sonido(self):
        return "Miau"

perro=Perro()
gato=Gato()
print(perro.sonido())
print(gato.sonido())


    #4- POLIMORFISMO
    #Diferentes clases pueden responder de manera distinta a la misma llamada de método

def hacer_sonido(animal):
    print(animal.sonido())

hacer_sonido(Perro())
hacer_sonido(Gato())


    #5- ABSTRACCIÓN
    #Oculta detalles complejos y expone solo las funcionalidades esenciales
    #Se implementa mediante clases y métodos abstractos

from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

rectangulo = Rectangulo(4, 5)
print(rectangulo.area())