### CONDICIONALES (if, elif, else)
# Es la estructura que nos permite tomar un flujo u otro según una condición

# La palabra reservada if es obligatoria en la estructura condicional pero elif y else son opcionales

a = 5
b = 9
c = 7

if a > b: # Si cumple esta condición hace 
    print(f"{a} es mayor que {b}") # estas lineas de código
elif c > b: # Si no cumple la primera condición pero cumple esta realiza:
    print(f"{c} es mayor que {b}") # estas otras líneas de código
else: # Si no cumplió ninguna de las condiciones anteriores
    print(f"{a} es menor que {b} y {c} es menor que {b}") # realiza estas últimas líneas de código


### Ejemplo:

# Objetivo entrar al boliche

edad = 61

if edad >= 18 and edad <= 60:
    print("Puedes entrar al boliche")
else: 
    if edad < 18:
        print("No tienes la edad suficiente para ingresar al boliche")
    else:
        print("Este boliche sólo admite personas hasta 60 años")


### SHORTHANDS

a = 5
b = 2

if a > b: print(f"{a} es mayor que {b}") ## Shorthand del If solo

# Ejecución si es verdadero | condición | Ejecución si es Falso
print("B es mayor que A") if b > a else print("A es mayor que B") ## Shorthand de If + Else 

######## 

"""  
IF / ELIF / ELSE 
"""  # control de condiciones 

#Condicion binaria

llueve = True
if llueve:
    print("Cogere el paraguas")
else:
    print("Ire a pasear") 

print("Resto del codigo") 


####



 #Ejercicio:  Vamos a preguntar la edad al usuari, si tiene menos 12 años -> Eres un niño/a
 #si tiene menos de 18 años -> Eres un adolecesnte 
 #si tienes menos de 30 años ->  Eres muy joven 
 #si tienes menos de 40 años -> pues eres joven, pero menos 
 # si tienes mas -> tu  puedes con todo 

 

# edad = int(input("Escribe tu edad -> "))
# if  0<= edad < 12:
#     print("Eres un niño/a")
# elif edad < 18:
#     print("Eres un adolecente")
# elif edad < 30:
#     print("Eres muy joven")
# elif edad < 40:
#     print("Eres joven pero menos") 
# else: 
#     print("Puedes con todo")


#Preguntar al usuario la edad
# si tiene menos de 0 o mas de 120 diremos: no me lo creo
#si tiene menos de 18 diremos : aun no puedes votar 
# si tienes menos de 18 diremos : aun no puedes votar, te faltan x años
# si tienes 18 o mas, diremos : puedes votar desde hace x años 

# Preguntar al usuario la edad

# edad = int(input("Por favor, escribe tu edad -> ")) 
# if edad < 0 or edad > 120:
#     print("No me lo creo")
# elif edad < 18:
#     print("Aun no puedes votar, te faltan {18 - edad} años")
#     edad = edad - 18
#     print(f"Te faltan {edad} años")
# else:
#     print("Puedes votar desde hace 18 años")
#     edad = edad - 18
#     print(f"Puedes votar desde hace {edad} años")

#Ejercicio
#pedir al usuario un numero 
#pedir otro numero 
#si no son numeros le diremos que no se puede hacer 
#pedir que operacion matematica quiere hacer ( 7 posibilidades suma, resta, división, 
# multiplicacion, exponente, division entera, modulo) 

#pero si no es ninguna de esras mostraremos un mensaje de error
#si divide por cero tambiebn mostraremos un mensaje



# num_1= float(input("Escribe el primer numero ->"))
# num_2= float(input("Escribe el primer numero ->"))
# operacion = input("¿Qué operación matemática quieres hacer ? ") 


# if operacion == "suma": 
#     resultado = num_1 + num_2 
#     print(f"El resultado de la suma es: {resultado}")

# elif operacion == "resta": 
#     resultado= num_1 - num_2
#     print(f"El resultado de la resta es: {resultado}")

# elif operacion == "división": 
#     if num_2 == 0: 
#         print("Error: No se puede dividir por cero.")
#         exit()
#     resultado = num_1 / num_2

#     print(f"El resultado de la división es: {resultado}")
# elif operacion == "multiplicacion": 
#     resultado = num_1 * num_2
#     print(f"El resultado de la multiplicacion es: {resultado}")

# elif operacion == "exponente": 
#     resultado = num_1 ** num_2
#     print(f"El resultado de la exponenciación es: {resultado}")

# elif operacion == "division entera": 
#     if num_2 == 0: 
#         print("Error: No se puede dividir por cero.")
#         exit()
#     resultado = num_1 // num_2
#     print(f"El resultado de la división entera es: {resultado}")
# elif operacion == "modulo": 
#     if num_2 == 0: 
#         print("Error: No se puede dividir por cero.")
#         exit()
#     resultado = num_1 % num_2
#     print(f"El resultado de la división entera es: {resultado}")
# else: 
#     print("Error: Operación no válida.")
#     exit()





# agregar que al pedir un caracter no numerico ( letras ) se muestre un mensaje de error 
#y volver que operacion deseas realizar


# --------------------------------------- 


# #variable para determinar la mayoria de edad
 
# mayoria_edad = 18

# #Obtenemos la edaad del usuario 
# edad = input("Por favor, escribe tu edad -> ")

# #Ninguno de estos metodos sirven para decimales 
# #print(edad.isdigit())
# #print(edad.isdecimal())
# #print(edad.isnumeric())
# #print(edad.isalpha()) 

# if not edad.isdigit():  #Comprobacion de que no sea introduco un numero entero 
#     print("Debes introducir un numero entero")
# elif 0 > int(edad) > 120: #Comprovamos del rango de edad valida 
#     print("No me lo creo")
# else: 
#     edad = int(edad) #Convierto a numero entero
#     diferencia = abs(mayoria_edad - edad)
# if edad < mayoria_edad: 
#     print(f"Aun no puedes votar, te faltan {diferencia} años")
# else: 
#     print(f"Puedes votar desde hace {diferencia} años") 


# #Ejercicios 

# num_1 = input("Escribe el primer numero -> ")
# #provar "1" , "1.2", "uno", "?"

# if num_1.isalpha(): 
#     print("No se puede hacer")


# -------------------------------- 



# import os
# os.system("")

# try: #intenta hacer algo
#     # Pedir números
#     numero1 = float(input("Introduce el primer número: "))  
#     numero2 = float(input("Introduce el otro número: "))
    
#     # Pedir operación
#     operacion = input("Introduce la operación a realizar (suma, resta, multiplicación, división, división_entera, modulo): ")

#     # Realizar operación
#     if operacion == "suma":
#         resultado = numero1 + numero2
#         print(f"El resultado de la suma es {resultado}")

#     elif operacion == "resta":
#         resultado = numero1 - numero2
#         print(f"El resultado de la resta es {resultado}")

#     elif operacion == "multiplicacion":
#         resultado = numero1 * numero2
#         print(f"El resultado de la multiplicación es {resultado}")

#     elif operacion == "division":
#         resultado = numero1 / numero2
#         print(f"El resultado de la división es {resultado}")

#     elif operacion == "division_entera":
#         resultado = numero1 // numero2
#         print(f"El resultado de la división entera es {resultado}")

#     elif operacion == "modulo":
#         resultado = numero1 % numero2
#         print(f"El resultado del módulo es {resultado}")

#     else:
#         print("Operación no válida")

# except ValueError:
#     print("Error: Debes ingresar un número válido.")

# except ZeroDivisionError:
#     print("Error: No se puede dividir por cero.")

# except Exception as e:
#     print(f"Ocurrió un error inesperado: {e}")

# print("El programa continúa.")



# # se puede producir una excpecion a causa de lo que introduzca el usuario 
# try: 
#     #pedimos los numeros
#     num_1 = float(input("Escribe el primer número -> "))
#     num_2 = float(input("Escribe el segundo número -> "))
#     print( '''
# Opciones:
#           suma
#           resta
#           multplicacion
#           division
#           división_entera
#           modulo
# ''')
#     operacion = input("¿Qué operación quieres realizar?")
#     if operacion == "suma":
#         print(f"{num_1} + {num_2} = {num_1 + num_2}")

#     elif operacion == "resta":
#         print(f"{num_1} - {num_2} = {num_1 - num_2}")

#     elif operacion == "multiplicacion":
#         print(f"{num_1} * {num_2} = {num_1 * num_2}")

#     elif operacion == "division":
#         print(f"{num_1} / {num_2} = {num_1 / num_2}")

#     elif operacion == "división_entera":
#         print(f"{num_1} // {num_2} = {num_1 // num_2}")

#     elif operacion == "exponente":
#         print(f"{num_1} ** {num_2} = {num_1 ** num_2}")

#     elif operacion == "modulo":
#         print(f"{num_1} % {num_2} = {num_1 % num_2}")

#         #####3



# except ValueError:
#     print("Debes introducir un numero valido en cifras")
   

# try:
#     #pedimos los numeros
#     num_1 = float(input("Escribe el primer número -> "))
#     num_2 = float(input("Escribe el segundo número -> "))
#     print( '''
# Opciones:
          
# ''')
#     operacion = input("¿Qué operación quieres realizar?")
#     match operacion:
#         case "suma":
#             print(f"{num_1} + {num_2} = {num_1 + num_2}")
#         case "resta":
#             print(f"{num_1} - {num_2} = {num_1 - num_2}")
#         case "multiplicacion":
#             print(f"{num_1} * {num_2} = {num_1 * num_2}")
#         case "division":
#             print(f"{num_1} / {num_2} = {num_1 / num_2}")
#         case "división_entera":
#             print(f"{num_1} // {num_2} = {num_1 // num_2}")
#         case "exponente":
#             print(f"{num_1} ** {num_2} = {num_1 ** num_2}")
#         case "modulo":
#             print(f"{num_1} % {num_2} = {num_1 % num_2}")
#         case _:
#             print("Opcion no valida")
# except ValueError:
#     print("Error: Debes introducir un numero valido...")


# try:
#     # Pedimos los números y la operación en una sola frase
#     respuesta = input("Indique los numeros y la operaion a realizar . \nEjemplo : 10, 5, + -> ").split(",")
#     num_1 = int(respuesta[0].strip())
#     num_2 = int(respuesta[1].strip())
#     operacion = respuesta[2].strip()
    

#     match operacion:
#         case "+": 
#             print(f"{num_1} + {num_2} = {num_1 + num_2}")
#         case "-":
#             print(f"{num_1} - {num_2} = {num_1 - num_2}")
#         case "*":
#             print(f"{num_1} * {num_2} = {num_1 * num_2}")
#         case "/":
#             if num_2 == 0:
#                 raise ZeroDivisionError("No se puede dividir por cero.")
#             print(f"{num_1} / {num_2} = {num_1 / num_2}")
#         case "//":
#             if num_2 == 0:
#                 raise ZeroDivisionError("No se puede dividir por cero.")
#             print(f"{num_1} // {num_2} = {num_1 // num_2}")
#         case "**":
#             print(f"{num_1} ** {num_2} = {num_1 ** num_2}")
#         case "%":
#             if num_2 == 0:
#                 raise ZeroDivisionError("No se puede dividir por cero.")
#             print(f"{num_1} % {num_2} = {num_1 % num_2}")
#         case _:
#             print("Opción no válida")
# except ValueError as e:
#     print(f"Error: {e}")
# except ZeroDivisionError as e:
#     print(f"Error: {e}")


# # Pedir al usuario que diga la frase
# #que si en la frase hay palindromo 


# def es_palindromo(frase):
#     # Eliminar espacios y convertir a minúsculas
#     frase_limpia = frase.replace(" ", "").lower()
#     # Comparar la frase con su versión invertida
#     return frase_limpia == frase_limpia[::-1]

# # Pedir al usuario que diga la frase
# frase = input("Introduce una frase: ")

# # Comprobar si la frase es un palíndromo
# if es_palindromo(frase):
#     print("La frase es un palíndromo.")
# else:
#     print("La frase no es un palíndromo.")


# # 

# frase = ""
# palabras_en_frase = frase.split() 
# print(palabras_en_frase)
# print(len(palabras_en_frase))



def es_palindromo(frase):
   
    frase_limpia = frase.replace(" ", "").strip()  # Eliminar espacios y convertir a minúsculas

    frase_invertida = frase_limpia[::-1]  # Invertir la frase
    
    return frase_limpia == frase_invertida, frase_invertida  # Comparar la frase con su versión invertida


frase = input("Introduce una frase: ") # Pedir al usuario que diga la frase

es_palindromo, frase_invertida = es_palindromo(frase) # Comprobar si la frase es un palíndromo y obtener la frase invertida


print(f"La frase invertida es: {frase_invertida}") # Mostrar la frase invertida

if es_palindromo:
    print("La frase es un palíndromo.")
else:
    print("La frase no es un palíndromo.")
          
      