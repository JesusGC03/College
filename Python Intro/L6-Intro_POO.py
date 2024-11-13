#############################################################################################################################
# Para comenzar la programacion orientada a objetos, debemos tener claro antes algunos matices                              #
# ->Una clase es un modelo que caracteriza un grupo, por ejemplo arboles o mamíferos                                        #
# ->Un objeto es un ejemplo de la clase, que pueda ser descrito y distinguido por sus caracteristicas, como roble o perro   #
# ->Una instancia de clase es un objeto ya definido perteneciente a una de las clases tambien definidas                     #
# ->Un modulo es una parte del programa que funciona de forma independiente al programa principal por su funcionamiento     #
# ->El encapsulamiento es el funcionamiento interior de cada modulo                                                         #
# ->Una funcion es un conjunto de instrucciones que logran realizar una tarea especifica                                    #
# ->Un metodo es una funcion que describe los usos que se le pueden dar a un objeto                                         #
#############################################################################################################################

#Ejemplo 1

class Libro():                                  #Declaramos la clase "Libro", junto a sus atributos
    Tamaño="10x20"
    Peso="200 g"
    Paginas="350"
    Registrado=False
    Coleccion="NoSe"
    Precio="20"

    def Registrar(self):                        #Estos metodos estan declaradas dentro de la clase, para que
        self.Registrado=True                    #cuando sean llamadas, el programa las encuentre
        return "Registrado"

    def Inscribir(self):
        self.Coleccion="Programacion"
        return self.Coleccion

ProgPython=Libro()                              #Aqui creamos el objeto tipo "Libro"
print("Tamaño: ", ProgPython.Tamaño)
print("Peso: ", ProgPython.Peso)
print("Páginas: ", ProgPython.Paginas)
print("Registro: ", ProgPython.Registrar())
print("Coleccion: ", ProgPython.Inscribir())
print("Precio: ", ProgPython.Precio)


#Ejercicio 1
#Construir programa que declare una clase tipo animal y que instancie un objeto llamado insecto
#4 atributos y 3 metodos

class Animal():
    Patas=0
    Mamifero=True
    Vertebrado=True
    Carnivoro=True

    def patas(self):
        self.Patas=8
        return self.Patas

    def mam(self):
        self.Mamifero=False
        return self.Mamifero

    def vert(self):
        self.Vertebrado=False
        return self.Vertebrado

    def carn(self):
        self.Carnivoro=True
        return self.Carnivoro


Insecto=Animal()
print("Patas: ", Insecto.Patas)
print("Mamífero: ", Insecto.Mamífero)
print("Vertebrado: ", Insecto.Vertebrado)
print("Carnivoro: ", Insecto.Carnivoro)