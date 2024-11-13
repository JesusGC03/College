#################################################################################################################
# De primera leccion de python, vemos las variables                                                             #
# Al contrario de C, nosotros nombramos las variables directamente poniendo su nombre y su valor                #
# P.E. -> si ponemos Var1 = 5 , se nos asignará una variable llamada "Var1" cuyo valor es un 5 (int)            #
# Tenemos variables tipo int, float, bool, complex y str (strings)                                              #
# Vamos a ver diferentes ejemplos                                                                               #
#################################################################################################################

# Ejemplo 1
Var1 = 5
Var2 = 10
Var3 = Var1 + Var2
print(Var3)


# Ejemplo 2
Var4 = "Hola"
Var5 = "Mundo"
print(Var4+" "+Var5)    #Podemos desplegar las variables de esta forma, o como hicimos en C (%s para strings, %f para float...)


#Ejemplo 3
Var6 = 3
Var7 = "Valor = "
Var7 += str(Var6)   #El comando str es para tomar Var6 que en principio es un int, por una variable de string
print(Var7)


#Ejemplo 4
Var8 = "Unamuno"                    #Como vemos aqui, el segundo string lo podemos encontrar en el primero
Var9 = "uno"                        #Este empieza en la posicion 4, ya que la primera posicion siempre la contamos como 0
BuscarEnCadena = Var8.find(Var9)    #La funcion .find nos permite encontrar un string dentro de otro
print(BuscarEnCadena)


#Ejemplo 5
Var10 = "Unamuno"
ExtraerCadena = Var10[2:6]          #De esta manera, podemos extraer ciertos caracteres del string que queramos
print(ExtraerCadena)