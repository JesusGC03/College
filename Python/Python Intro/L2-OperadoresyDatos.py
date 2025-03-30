#################################################################################################################
# En python tenemos algunos operadores iguales a C, pero hay otros diferentes y nuevos                          #
# La suma, resta, división, multiplicacion, y la division que recoge el resto son iguales                       #
# Hay dos operadores nuevos, el exponencial (**) y la division entera (//) que obtiene el cociente              #
# Como también nos pasaba en C, al poner "\n" en la funcion print, realizaremos un salto de línea               #
# Tambien tendremos la funcion input, que será como el scanf en C que ahora veremos como usarla                 #
#################################################################################################################


#Ejercicio 1
Var1 = 3
Var2 = 12
Var3 = Var1 + Var2
Var4 = Var2 - Var1
Var5 = Var2 / Var1
Var6 = Var2 % Var1
Var7 = Var2 // Var1
Var8 = Var2 ** Var1

print("la suma realizada es: ", Var3)
print("la resta realizada es: ", Var4)
print("la division realizada es: ", Var5)
print("el modulo realizado es: ", Var6)
print("la division entera realizada es: ", Var7)
print("el exponente realizado es: ", Var8)


#Ejercicio 2
varEntero=int(input("\nIntroduce un número entero pequeño: "))      #Se puede usar poniendo primero el tipo de variable que es, o simplemente poniendo la funcion
varLargo=int(input("Introduce un número entero largo: "))
varReal=float(input("Introduce un número real: "))
varComplex=complex(input("Introduce un número complejo (A+Bj): "))
varCadena=str(input("Introduce una cadena de caracteres: "))
varBoolean=bool(input("Introduce un Booleano (True/False): "))

print("\nEste es un numero entero corto: ", varEntero)
print("Este es un numero entero largo: ", varLargo)
print("Este es un numero real: ", varReal)
print("Este es un numero complejo: ", varComplex)
print("Esta es una cadena de caracteres: ", varCadena)
print("Esta es un Booleano: ", varBoolean)



#Ejercicio de ejemplo extra 1
#Construir un programa que reciba dos numeros enteros y calcule el resultado de elevar el primer número por
#   el segundo

Var10 = int(input("\n\nIntroduce el primer número: "))
Var20 = int(input("Introduce el segundo numero: "))
Var30 = Var10 ** Var20
print("\nEl resultado es: ", Var30)