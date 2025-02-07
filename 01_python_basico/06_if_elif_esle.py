"""
IF / ELIF / ELSE
Control de condiciones
"""

import os
os.system("cls")

'''
# Condición binaria 
llueve = True

if llueve:
    print("Cogeré el paraguas")
else:
    print("Iré a pasear")

print("Resto del código")



lunes = False # los lunes como pizza
jueves = True # jueves, paella
# el resto de días un bocadillo

if lunes:
    print("toca pizza")
elif jueves:
    print("toca paella")
else:
    print("toca bocadillo")
'''
# Ejercicio: 
# Preguntar la edad al usuario
# si tiene menos de 12 años -> eres un niño/a
# si tiene menos de 18 -> eres un/a adolescente
# si tiene menos de 30 -> eres muy joven
# si tiene menos de 40 -> eres joven, pero menos
# si tiene más o igual a 40 -> tu puedes con todo

'''
edad = int(input("por favor, indica tu edad -> "))
# edad = int(edad)

if 0 <= edad < 12:
    print("eres un niño/a")
elif edad < 18:
    print("eres un/a adolescente")
elif edad < 30:
    print("eres muy joven")
elif edad < 40:
    print("eres joven, pero menos")
elif edad < 120 :
    print("tu puedes con todo")
else:
    print("no me lo creo")
'''

'''
# Ejercicio: 
# Preguntar al usuario la edad
# si tiene menos de 0 o más de 120 diremos : no me lo creo
# si tiene menos de 18 diremos : aun no puedes votar, te faltan x años
# si tiene 18 o más, diremos : puedes votar desde hace x años

# Variable para determinar la mayoría de edad
mayoria_edad = 18
# Obtenemos la edad del usuario
edad = input("Por favor indica tu edad -> ")

# Ninguno de estos métodos sirven para decimales
# print(edad.isdigit())
# print(edad.isdecimal())
# print(edad.isnumeric())
# print(edad.isalpha())

if not edad.isdigit(): # Comprobación de que no se ha introducido un número entero
    print("Debes introducir un número entero")
elif 0 > int(edad) > 120: # Comprobación del rango de edad válida
    print("No me lo creo")
else:
    edad = int(edad) # Convertimos la edad a un número entero
    diferencia = abs(mayoria_edad-edad)

    if edad < mayoria_edad:
        print(f"Aun no puedes votar, te faltan {diferencia} años")
    else:
        print(f"Puedes votar desde hace {diferencia} años")




   '''


# Ejercicio
# pedir al usuario un número
# pedir otro número
# si no son números cada uno le diremos que no se puede hacer
# pedir qué operación matemática quiere hacer (7 posibilidades)
#     suma
#     resta
#     multi
#     division
#     exp
#     div_ent
#     modulo
# pero si no es ninguna de estas mostraremos un mensaje de error
# si divide por cero también mostraremos un mensaje
#
# Al final debe aparecer algo así :
# Escriba el primer número -> 1
# Escriba el segundo número ->3
# ¿Qué operación quiere realizar? suma
# 1 + 3 = 4

'''


# num_1 = float(input("Escriba el primer número -> "))
# # provar "1", "1.2", "uno", "??"
# if num_1.isalpha():
#     print("No se puede hacer")
# else:
#     print("Se puede hacer")

'''
# Se puede producir una excepción a causa de lo que introduzca el usuario
print("Solución 1")
try: 
    # Pedimos los números
    num_1 = float(input("Escriba el primer número -> "))
    num_2 = float(input("Escriba el segundo número -> "))
    print('''
Opciones:
          suma
          resta
          multiplicacion
          division
          división_entera
          exponente
          modulo
''')
    operacion = input("¿Qué operación quiere realizar? ")

    if operacion == "suma":
        print(f"{num_1} + {num_2} = {num_1 + num_2} ") 
    elif operacion == "resta":
        print(f"{num_1} - {num_2} = {num_1 - num_2} ") 
    elif operacion == "multiplicacion":
        print(f"{num_1} * {num_2} = {num_1 * num_2} ") 
    elif operacion == "division":
        print(f"{num_1} / {num_2} = {num_1 / num_2} ") 
    elif operacion == "division_entera":
        print(f"{num_1} // {num_2} = {num_1 // num_2} ") 
    elif operacion == "exponente":
        print(f"{num_1} ** {num_2} = {num_1 ** num_2} ") 
    elif operacion == "modulo":
        print(f"{num_1} % {num_2} = {num_1 % num_2} ") 
    else:
        print("No se reconoce la operación")
except ValueError:
    print("Debes introducir un número válido en cifras")
except ZeroDivisionError:
    print("No puedes dividir por 0")  # Para cualquier división por 0

print("Solución 2")
try: 
    # Pedimos los números
    num_1 = float(input("Escriba el primer número -> "))
    num_2 = float(input("Escriba el segundo número -> "))
    print('''
Opciones:
          suma
          resta
          multiplicacion
          division
          división_entera
          exponente
          modulo
''')
    operacion = input("¿Qué operación quiere realizar? ")

    match operacion :
        case "suma":
            print(f"{num_1} + {num_2} = {num_1 + num_2} ") 
        case "resta":
            print(f"{num_1} - {num_2} = {num_1 - num_2} ") 
        case "multiplicacion":
            print(f"{num_1} * {num_2} = {num_1 * num_2} ") 
        case "division":
            print(f"{num_1} / {num_2} = {num_1 / num_2} ") 
        case "division_entera":
            print(f"{num_1} // {num_2} = {num_1 // num_2} ") 
        case "exponente":
            print(f"{num_1} ** {num_2} = {num_1 ** num_2} ") 
        case "modulo":
            print(f"{num_1} % {num_2} = {num_1 % num_2} ") 
        case _ :
            print("No se reconoce la operación")
except ValueError:
    print("Debes introducir un número válido en cifras")
except ZeroDivisionError:
    print("No puedes dividir por 0")  # Para cualquier división por 0


print("Solución 3")
try:
    respuesta = input("Indique los números y la operación a realizar.\nEjemplo : 10, 5, +").split(", ")
    num_1 = float(respuesta[0])
    num_2 = float(respuesta[1])
    operacion = respuesta[2]

    match operacion:
        case "+" | "-" | "*" | "/" | "**" | "//" | "%":
            resultado = eval(f"{num_1} {operacion} {num_2}")
            print(f"{num_1} {operacion} {num_2} = {resultado}")
        case _ :
            print("Operación desconocida. Revise la entrada de datos")


except ValueError:
    print("Debes introducir un número válido en cifras")
except ZeroDivisionError:
    print("No puedes dividir por 0")  # Para cualquier división por 0



