#####################################################################################################################
# Al igual que las funciones en C, sirven para simplificar el código y la resolucion de errores                     #
# Definiremos las funciones al principio del programa, y las definiremos como: "def Funcion (variables): <accion>"  #
#####################################################################################################################

#Ejercicio 1
    #Construir una funcion que reciba tu nombre como parámetro y lo muestre 5 veces

def MuestraNombre(nombre):
    for i in range(5):
        print(nombre)

nombre=input("Introduce tu nombre: ")
MuestraNombre(nombre)


#Ejercicio 2
    #Construir una funcion que reciba una lista de datos numéricos y muestre la suma de ellos

def SumaNums(*num):
    cont=sum(num)                               #La funcion "sum(), nos permite realizar la suma de una lista númerica que le demos."
    return cont

suma=SumaNums(1,2,3,4,5)
print("la suma total es: ", suma)


#Ejercicio 3
    #Construir una funcion que reciba un valor entero y muestre su tabla de multiplicar

def Tabla(num):
    resultado=0
    for i in range(1,11):
        resultado=num*i
        print(resultado)

numero=int(input("De qué número quieres la tabla de multiplicar: "))
Tabla(numero)