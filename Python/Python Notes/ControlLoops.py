#########################################################################
# Resumen de las estructuras de control utilizadas en python            #
# Separadas en condicionales, bucles, controles de flujo y comparadores #
#########################################################################


# Sentencias Condicionales #

    #1- IF
    #Evalúa una condición y, si es verdadera, ejecuta el bloque de código

numero=int(input("Introduce un número: "))

if numero>0:
    print(f"El número {numero} es positivo.\n")



    #2- IF ELSE
    #Evalúa una condición y ejecuta uno de dos bloques según sea verdadera o falsa

if numero%2==0:
    print("Es par.\n")
else:
    print("Es impar.\n")


    #3- ELIF
    #Permite manejar múltiples condiciones de forma más legible

if numero >= 90:
    print("A\n")
elif numero >= 80:
    print("B\n")
else:
    print("C\n")


# Bucles #

    #1- FOR
    #Itera sobre elementos de un iterable

for i in range(4):
    print(i)
print("\n")


    #2- FOR ELSE
    #Ejecuta un bloque adicional si el bucle termina sin interrupción

for i in range(5):
    if i == 3:
        break
else:
    print("Bucle completado sin interrupciones\n")


    #3- WHILE
    #Repite mientras la condición sea verdadera

contador = 0
while contador < 5:
    print(contador)
    contador += 1
print("\n")


# Control de Flujo #

    #1- BREAK
    #Termina el bucle actual

for i in range(10):
    if i == 5:
        break
    print(i)
print("\n")


    #2- CONTINUE
    #Salta a la siguiente iteración del bucle

for i in range(5):
    if i == 5:
        continue
    print(i)
print("\n")


    #3- PASS
    #Actúa como un marcador de posición sin realizar ninguna acción

for i in range(5):
    if i == 3:
        pass
    print(i)
print("\n")


# Comparadores #

    #1- IS/IS NOT
    #Comparan la identidad de dos objetos

a = [1, 2, 3]
b = a
c = a[:]
print(a is b)  # True, misma referencia
print(a is c)  # False, diferente objeto
print("\n")


    #2- Operador
    #Una forma compacta de realizar asignaciones condicionales

edad=int(input("Introduce una edad:"))
estado = "Adulto" if edad >= 18 else "Menor"
print(f"{estado}\n")