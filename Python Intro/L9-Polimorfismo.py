#############################################################################################################################
# El polimorfismo nos permite cambiar de forma a un objeto fácilmente. Para verlo mejor, me apoyaré en el Ejemplo 1         #
#                                                                                                                           #
# En el Ejemplo 1, están definidas 3 clases, Persona, Animal y Arbol, y cada una de ellas con una funcion "identificación"  #
# Una vez habiendo declarado las varialbes Hombre, Mascota y Planta, llamamos a sus funciones "identificacion", pasandoles  #
# sus respectivos nombres (Carla, Tommy, Clavel). El resultado será que cada objeto llamará a su respectiva funcion para    #
# realizarla, saliendo por pantalla las frases de los metodos, con los nombres anteriores (Carla, Tommy, Clavel).           #
#                                                                                                                           #
# Si nos fijamos bien, nos podremos dar cuenta de que cada funcion de identificacion es prácticamente igual a las demás,    #
# con la diferencia del tipo de ser vivo al que nos refiramos, aqui entra en juego el polimorfismo.                         #
# El polimorfismo nos va a permitir que, creando una nueva función fuera de las clases, que recibirá los parámetros         #
# "SerVivo" y "nombre". SerVivo nos permitirá ir adaptando la clase de objetos segun el objeto que le llame, es decir,      #
# si el objeto "Hombre" llama a la función "general", y esta funcion, al ser llamada por un objeto de clase "Persona",      #
# adopta la clase "Persona()" y llama a la funcion de esta clase, por lo que el objeto Hombre mostrará por pantalla el mensaje  #
# de la clase "Persona()" #
#############################################################################################################################


#Ejemplo 1

class Persona():
    def identificacion(self, nombre):
        print(f"Me llamo {nombre}, y soy humano")

class Animal():
    def identificacion(self, nombre):
        print(f"Me llamo {nombre}, y soy un animal")

class Arbol():
    def identificacion(self, nombre):
        print(f"Me llamo {nombre}, y soy un arbol")


def general(SerVivo, nombre):
    SerVivo.identificacion(nombre)

Hombre=Persona()
Mascota=Animal()
Planta=Arbol()

Hombre.identificacion("Carla")
Mascota.identificacion("Tommy")
Planta.identificacion("Clavel")
print("\n")
general(Hombre, "Carlos")
general(Mascota, "Nala")
general(Planta, "Rosa")

print("\n")



#Ejercicio 1
    #Utiliza el polimorfismo para mostrar los siguientes datos: Ordenador, Tablet, Movil.

class Ordenador():
    def identify(self, marca):
        print(f"Soy un ordenador de la marca {marca}")

class Tablet():
    def identify(self, marca):
        print(f"Soy una tablet de la marca {marca}")

class Movil():
    def identify(self, marca):
        print(f"Soy un movil de la marca {marca}")


def todo(cosa, marca):
    cosa.identify(marca)


PC=Ordenador()
Tab=Tablet()
Cell=Movil()

todo(PC, "Lenovo")
todo(Tab, "Huawei")
todo(Cell, "Apple")