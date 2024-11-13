#################################################################################################################
# Los condicionales en python funcionan igual que en C, la unica diferencia es la sintaxis del ifelse --> ifel  #
# Para poder realizar el condicional, escribiremos el condicional "if", seguido de la comprobacion que queramos #
# Al igual que en C, si es True, realizará lo asignado en el if, si es False, realizará lo asignado al else     #
# Tendremos que poner siempre una sentencia if, y una sentencia else, terminando ambas con un ":"               #
# Al igual que en C, también podremos hacer condicionales con dos comprobaciones, con los operadores designados #
# Hay 3 operadores lógicos y 6 operadores relacionales                                                          #
# Los relacionales son >, <, >=, <=, ==, y, !=, al igual que en C                                               #
# Los lógicos son "and" (dos iguales), "or" (una u otra), y "not" (ninguna de las dos)                          #
#################################################################################################################


#Ejercicio 1
    #Vamos a comprobar si el número recibido es el 10
Var1 = int(input("Introduce un número entero: "))
if Var1 == 6:
    print("El número es el 6.")
else:
    print("El número no es el 6.")


#Ejercicio 2
    #Ahora vamos a comprobar que el numero recibido tiene 3 dígitos
Var2 = int(input("\nIntroduce un número de 3 dígitos: "))
if Var2 <= 999 and Var2 >= 100:
    print("El número tiene 3 dígitos.")
else:
    print("El número no tiene 3 dígitos.")


#Ejercicio 3
    #Nos piden realizar un programa para calcular el promedio de ventas de los empleados en una tienda.
Nombre = str(input("\n\nIntroduce el nombre del trabajador: "))
Mes1 = int(input("Introduce las ganancias del primer mes: "))
Mes2 = int(input("Introduce las ganancias del segundo mes: "))
Mes3 = int(input("Introduce las ganancias del tercer mes: "))

Prom = (Mes1 + Mes2 + Mes3) / 3

    #Para hacerlo mas interesante, vamos a hacer que si no ha llegado a un minimo de 2000, le tenemos que despedir

print("\n\nGanancias del trabajador ", Nombre)
if Prom < 2000:
    print("Sus ganancias están por debajo de lo previsto, se requiere un despido inmediato.")
else:
    print("Sus ganancias están por encima de lo previsto, se le realizará un aumento del sueldo.")

    #Si quisieramos poner las ganancias totales, nos saldría con muchos decimales, para no hacer eso usamos el comando "round"

print("\nSus ganancias han sido: ", round(Prom,2))

    #De esta manera, recortaremos el numero de decimales a solo 2.