#############################################################################################
# Resumen de Herencia en Python                                                             #
# La herencia permite a una clase basarse en otra clase, heredando sus atributos y métodos  #
#############################################################################################


# Introducción a las Herencias #

    #1- DEFINICIÓN Y SINTAXIS
    #Usar paréntesis para especificar la clase base.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice Miau"
    
gato = Gato("Pelusa")
print(gato.hablar())



    #2- CONTROL DE ACCESO
    #Hay tres niveles de acceso: público, protegido y privado
    #PÚBLICO -> Sin prefijo especial. Accesibles desde cualquier lugar.
    #PROTEGIDO -> Comienzan con un guión bajo. Accesibles en subclases.
    #PRIVADO -> Comienzan con un doble guión bajo. Utilizan "name mangling" para evitar colisiones de nombres.

class Animal:
    def __init__(self, nombre, ):
        self.nombrePublico = nombre
        self._nombreProtegidonombreProtegido = nombre
        self.__nombrePrivado = nombre


    #3- SOBREESCRITURA DE MÉTODOS
    #Nos permite redefinir un método de la clase base en una clase derivada.
    #Nos permite el polimorfismo.

class Animal:
    def hablar(self):
        return "Sonido Genérico"

class Perro(Animal):
    def hablar(self):
        return "Guau!"
    
perro = Perro()
print(perro.hablar())


    #4- USO DE "SUPER()"
    #Llama a métodos o inicializadores de la clase base.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza


    #5- DUCK TYPING
    #Evita el comportamiento de un objeto en lugar de su tipo explícito.

class Pato:
    def hablar(self):
        return "Cuac!"
    def volar(self):
        return "Estoy volando!"

class Persona:
    def hablar(self):
        return "Imitando a un pato!"
    def volar(self):
        return "Pretendiendo volar!"

def prueba(objeto):
    print(objeto.hablar())
    print(objeto.volar())

prueba(Pato())  
prueba(Persona())  


    #6- TIPOS DE HERENCIA
    #Simple: Una clase base.
    #Múltiple: Múltiples clases base.
    #Multinivel: Jerarquía de herencia con varios niveles.
    #Jerárquica: Varias clases derivadas de una clase base.
    #Híbrida: Combina tipos de herencia.

# Ejemplo de Herencia Múltiple #

class A:
    def metodo_a(self):
        return "Método A"

class B:
    def metodo_b(self):
        return "Método B"

class C(A, B):
    pass

c = C()
print(c.metodo_a())  # Salida: Método A
print(c.metodo_b())  # Salida: Método B


    #7- CLASES Y MÉTODOS ABSTRACTOS
    #CLASES ABSTRACTAS -> No se pueden instanciar, se usan como base para otras clases.
    #MÉTODOS ABSTRACTOS -> Deben implementarse en las clases derivadas

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau!"


    #8- MIXINS
    #Clases ligeras usadas para agregar funcionalidad adicional.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class TerrestreMixin:
    def caminar(self):
        return f"{self.nombre} camina."

class AcuaticoMixin:
    def nadar(self):
        return f"{self.nombre} nada."

class Perro(Animal, TerrestreMixin):
    pass

perro = Perro("Buddy")
print(perro.caminar())


    #9- DECORADORES Y HERENCIA
    #Los decoradores también se pueden heredar o sobrescribir.

def registrar(func):
    def envoltura(*args, **kwargs):
        print(f"Llamando a {func.__name__}")
        return func(*args, **kwargs)
    return envoltura

class Padre:
    @registrar
    def saludar(self):
        print("Hola desde Padre")

class Hijo(Padre):
    @registrar
    def saludar(self):
        super().saludar()
        print("Hola desde Hijo")

Hijo().saludar()
