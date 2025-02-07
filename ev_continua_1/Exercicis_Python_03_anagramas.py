"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 3
Un anagrama es un texto o palabra resultante de modificar el orden de otro texto o palabra.
Los textos deberán ir sin tildes (acentos o diéresis)
No se tienen en cuenta mayúsculas ni espacios.

Mostraremos el mensaje: "Anagramas"
Pediremos al usuario un texto/palabra.
Pediremos al usuario un segundo texto/palabra
Responderemos si ambos son anagramas o no.

Por ejemplo:
    "Introduzca el primer texto --> " Pedro
    "Introduzca el segundo texto --> " Poder
    "Son anagramas --> Sí"

Otro ejemplo:
    "Introduzca el primer texto --> " Ramon
    "Introduzca el segundo texto --> " Morir
    "Son anagramas --> No"
 
"""

print("Anagramas") # imprimimos el mensaje 

texto1= input("Introduzca el primero texto: ").replace(" ", "").lower() # pedimos al usuario que introduzca un texto y lo 
#convertimos a minúsculas y sin espacios y el replace reemplaza 
texto2= input("Introduzca el segundo texto: ").replace(" ", "").lower()  # colocamos lo mismo para ambos 

def  es_anagrama(texto1, texto2):  # definimos una funcion llamada es_anagrama que recibe dos argumentos 
    if len(texto1) != len(texto2):  # si los textos tienen distinto tamaño retorna False
        return False 

    return sorted(texto1) == sorted(texto2) # si son anagramas retorna True, si no retorna False

if es_anagrama(texto1, texto2):  # llamamos a la funcion si es anagrama y nos imprime Si o No 
    print("Son anagramas --> Sí") # si son anagramas imprimimos el mensaje
else: 
    print("Son anagramas --> No") # si no son anagramas imprimimos el mensaje
