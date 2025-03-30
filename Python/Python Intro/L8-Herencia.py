#############################################################################################################################
# La Herencia es un mecanismo de python que nos permite que una clase tenga los mismos métodos y atributos que otra clase   #
# Por ejemplo, si tenemos las clases: Ser Vivo, Animal, Mamífero. Tendríamos que la clase Mamífero hereda cosas de la clase #
# Animal, y esta clase a su vez hereda cosas de la clase Ser Vivo (Ser Vivo -> Animal -> Mamífero). Se ve claramente en el  #
# ejemplo siguiente.                                                                                                        #
#                                                                                                                           #
# Cabe resaltar, que una misma clase puede heredar de dos clases a la vez, es decir, Mamífero puede heredar las clases y    #
# atributos de Ser Vivo y de Animal (normalmente, heredará de la primera clase que le pongamos).                            #
#                                                                                                                           #
# Si queremos hacer referencia a un atributo o método de la clase de la que heredamos, utilizaremos la funcion "super()"    #
# Si queremos saber si un objeto está dentro de una clase, utilizaremos la función "isinstance(objeto, clase)"              #
#############################################################################################################################

#Ejemplo 1
    #Construccion de un programa con 3 clases, dos con constructores propios y la restante lo heredará de una de las otras.

class Impreso():
    def __init__(self):
        self.peso=0
        self.hojas=0
        self.precio=0

class Libro():
    def __init__(self, pesoL, hojasL, precioL):
        self.peso=pesoL
        self.hojas=hojasL
        self.precio=precioL

class Folleto(Libro):                               #No le ponemos ningun constructor, ya que esta heredando el constructor de la clase Libro
    pass                                            #Al ponerle la clase Libro entre los paréntesis, ya detecta que tiene que heredar de esa clase

Revista1=Impreso()
Libro1=Libro("111g", 111, 11111)
Folleto1=Folleto("222g", 222, 22222)

print("Revista1 Peso: ", Revista1.peso)
print("Revista1 Hojas: ", Revista1.hojas)
print("Revista1 Precio: ", Revista1.precio)
print("****************************************")
print("Revista1 Peso: ", Libro1.peso)
print("Revista1 Hojas: ", Libro1.hojas)
print("Revista1 Precio: ", Libro1.precio)
print("****************************************")
print("Revista1 Peso: ", Folleto1.peso)
print("Revista1 Hojas: ", Folleto1.hojas)
print(f"Revista1 Precio: {Folleto1.precio}\n\n")





#Ejercicio 1
    #Muestra tres datos de cada objeto, construyendo el siguiente esquema: Mamífero -> Doméstico -> Perro

class Mamifero():
    def __init__(self):
        self.patas=4
        self.pelo=True
        self.Comida="Omnivoros"

class Domestico(Mamifero):
    pass

class Perro(Domestico):
    pass

Mamifero1=Mamifero()
Domestico1=Domestico()
Perro1=Perro()


print("Revista1 Peso: ", Mamifero1.patas)
print("Revista1 Hojas: ", Mamifero1.pelo)
print("Revista1 Precio: ", Mamifero1.Comida)
print("****************************************")
print("Revista1 Peso: ", Domestico1.patas)
print("Revista1 Hojas: ", Domestico1.pelo)
print("Revista1 Precio: ", Domestico1.Comida)
print("****************************************")
print("Revista1 Peso: ", Perro1.patas)
print("Revista1 Hojas: ", Perro1.pelo)
print("Revista1 Precio: ", Perro1.Comida)
