#################################################################################################################
# Como en C, en python tambien existen los bucles for y los bucles while                                        #
# La sentencia que usaremos para el for, sera: "for <variable> in <condicion>: <accion>"                        #
# Tal y como en C, el bucle for seguirá haciendo la accion escrita mientras la variable cumpla la condición     #
# La sentencia para el while, sera: "while <condicion>: <accion>", y al igual que en C, solo se hará si es True #
# También tenemos las intrucciones "break", "continue", y "else", que podremos utilizar en los bucles           #
#################################################################################################################

#Ejercicio 1
    #Vamos a hacer que muestre por pantalla 10 veces la palabra 'Programacion'

for i in range(10):             #range es una funcion que nos permite delimitar un bucle como acabo de hacer, hará un conteo desde 0 hasta el numero definido
    print("Programacion")


#Ejercicio 2
    #Hacer que realice la suma de todos los numeros entre 1 y 1000

i=1
while i<=1000:
    print(i)
    i=i+1


#Ejercicio 3
    #Mostrar los numeros pares comprendidos entre 1 y 20, mostrar la suma de todos ellos

cont=0
for i in range(1,21):
    if i%2==0:
        cont=cont+i
print(cont)


#Ejercicio 4
    #Mostrar los numeros multiplos de 5 contenidos entre 13 y 48

for i in range(13,49):
    if i%5==0:
        print(i)


#Ejercicio 5
    #Cuenta los espacios en blanco de una frase introducida y muestralos

cont=0
frase=input("Introduce la frase: ")

for i in frase:
    if i==' ':
        cont=cont+1

print("\nLa frase tiene", i ,"espacios")


#Ejercicio 6
    #Mostrar el año en el que estamos de 1 a 5 veces, excepto cuando i=3

i=1
while i<=5:
    if i==3:
        i=i+1;
        continue
    else:
        i=i+1
        print("2024")


#Ejercicio 7
    #Mostrar el año en el que estamos de 1 a 5 veces, pero cuando i=3, se pare el bucle

i=1
while i<=5:
    if i==3:
        break;
    else:
        print("2024")
        i=i+1