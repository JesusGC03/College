#####################################################################################################################################
# Un constructor es un  metodo que permite crear condiciones iniciales para un objeto o instancia de clase                          #
# Encapsular consiste en diseñar una clase con algunas caracteristicas que solo se puedan modificar desde dentro y no desde fuera   #
#####################################################################################################################################

#Ejemplo 1

class Libro():                                  #Declaramos la clase "Libro", junto a sus atributos
    Tamaño=""                                   #Ahora tenemos 3 tipos de variables
    Peso=0                                      #Las que las digita el usuario
    Paginas=0                                   #Las que las digita la editorial
    PrecioxPag=0                                #Las que se calculan
    PesoxPag=0                                  #Las variables que digita el usuario necesitan un metodo que recibe el contenido y lo almacena donde corresponde
    PrecioVta=0                                 #Las que se calculan necesitaran un metodo para que se realice el calculo pertinente
    Titulo=""                                   #Para las que digita la editorial, crearemos un metodo constructor para almacenar estas variables de forma automática
    Tapa=""                                     #Para hacerlo en cualquier clase, el constructor se llama "__init__"
    URL=""
    ISBN=""
    Estado="No Registrado"

    def __init__(self):                         #Creamos el metodo constructor para que estas variables sean como lo quiere la editorial
        self.Tamaño="10x20"                     #Si quisieramos que estas variables solo se pudiesen modificar desde dentro, y no desde fuera
        self.PrecioxPag=300                     #tendriamos que "encapsularlas", poniendo dos guiones bajos despues del punto, es decir:
        self.PesoxPag=0.8                       #En esta variable tendriamos que poner self.__PesoxPag=0.8, y en la clase, tambien se los tendremos que poner

    def Registrar(self):
        Estado="Registrado"
        return Estado

    def TamañoLibro(self):
        return self.Tamaño

    def PrecioPag(self):
        return self.PrecioxPag

    def PesoPag(self):
        return self.PesoxPag

def MuestraDatos(Libro):
        print("Tamaño: ", Libro.TamañoLibro)
        print("Páginas: ", Libro.Paginas)
        print("Precio Venta: ", Libro.PrecioVta)
        print("Peso: ", round(Libro.Peso, 2))
        print("PrecioxPag: ", Libro.PrecioxPag)
        print("PesoxPag: ", Libro.PesoxPag)
        print("Título: ", Libro.Titulo)
        print("Tapa: ", Libro.Tapa)
        print("URL: ", Libro.URL)
        print("ISBN: ", Libro.ISBN)
        print("***********************************")

def DatosLibro(Libro, NumPags, Nombre, TipoTapa, URL, ISBN):
        Libro.Paginas=NumPags
        Libro.PrecioVta=NumPags*Libro.PrecioxPag
        Libro.Peso=Libro.PesoxPag*NumPags
        Libro.Titulo=Nombre
        Libro.Tapa=TipoTapa
        Libro.URL=URL
        Libro.ISBN=ISBN

def RecibeDatos(Libro):
        Nombre=input("Nombre del libro: ")
        NumPags=input("NumPags del libro: ")
        TipoTapa=input("Tapa Dura (D), Tapa Blanda (B): ")
        URL=input("URL? (S/N)")
        ISBN=input("ISBN: ")
        print("**********************************************************")
        DatosLibro(Libro, Nombre, NumPags, TipoTapa, URL, ISBN)


Libro1=Libro()
Libro2=Libro()

print("Datos Libro 1")
RecibeDatos(Libro1)