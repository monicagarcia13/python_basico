"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 1

Un número primo es aquel que sólo es divisible por sí mismo o uno.

Pediremos al usuario un número entero.
Si escribe algo que no sea un número entero la aplicación debe responder: 
    "Has de introducir un número entero".
Daremos hasta tres oportunidades para que nos facilite un dato correcto.
Pero si pasadas esas tres oportunidades sigue sin escribir un entero 
la aplicación finalizará mostrando este mensaje:
    "No has podido introducir un número entero en tres oportunidades
    Puedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación.
    ".
Si escribe un número entero puede pasar que
-- sea un número primo; en ese caso la respuesta de la aplicación será:
    "El número X es primo".
-- no sea un número primo; en ese caso la respuesta de la aplicación será:
    "El número X no es primo".

. 
"""

def es_primo(numero): # define una funcion llamada es_primo que recibe un argumento numero
    if numero < 2: # verifica si el numero es menor que 2
        return False # si es menor que 2, retorna False porque los números menores que 2 no son primos
    for i in range(2, numero): # itera desde 2 hasta el numero
        if numero % i == 0: # verifica si el numero es divisible por i
            return False #  si es divisible por i, retorna False porque el numero no es primo
    return True # retorna True porque el numero es primo

intentos = 3 # iniciamos la variable con los 3 intentos 

while intentos > 0: # creamos un bucle que se ejecuta mientras intentos sea mayor que 0
    entrada = input("Introduce un número entero: ")
    try: # hacemos un try para manejar posibles excepciones
        numero = int(entrada)
        if es_primo(numero):
            print(f"El número {numero} es primo.")
        else:
            print(f"El número {numero} no es primo.")
        break # responde al usuario que el numero es primo y sale del bucle
    except ValueError:
        print("Has de introducir un número entero.")
        intentos -= 1 # se resta por el numero de intentos

if intentos == 0:
    print("No has podido introducir un número entero en tres oportunidades.")
    print("Puedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación.")