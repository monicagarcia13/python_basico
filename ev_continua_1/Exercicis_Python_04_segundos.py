"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 4
Mostraremos el mensaje: "Conversor de segundos"
A continuación pediremos al usuario una cantidad de segundos.

Le responderemos:
- Si son menos de 60 segundos, mostrará "X segundos son menos de 1 minuto"
- Si es igual o superior a 60 segundos le diremos:
    "X segundos son Y minutos y Z segundos"

Y así para las siguientes unidades de tiempo. Por tanto, si la cantidad de segundos 
supera la hora, le diremos cuantas horas, minutos y segundos son. 
Lo mismo si supera un día o una semana. 

. 
"""


print("Conversor de segundos")  # imprimimos el mensaje
segundos = int(input("Por favor, introduzca la cantidad de segundos: "))  # pedimos al usuario que introduzca la cantidad de segundos 

if segundos < 60: # hacemos la condicion para segundos 
    print(f"{segundos} segundos son menos de 1 minuto")  # si son menos de 60 segundos imprimimos el mensaje
else: # el else es para minutos 
    minutos = segundos // 60  # calculamos el número de minutos
    segundos = segundos % 60  # calculamos el número de segundos restantes
    if minutos < 60: # hacemos la condicion para minutos
        print(f"{minutos} minutos y {segundos} segundos")  # si son menores de 60 minutos imprimimos el mensaje
    else: 
        horas = minutos // 60  # calculamos el número de horas
        minutos = minutos % 60  # calculamos el número de minutos restantes
        if horas < 24:
            print(f"{horas} horas, {minutos} minutos y {segundos} segundos")  # si son menores de 24 horas imprimimos el mensaje
        else:
            dias = horas // 24  # calculamos el número de días
            
            horas = horas % 24  # calculamos el número de horas restantes
            if dias < 7:
                print(f"{dias} días, {horas} horas, {minutos} minutos y {segundos} segundos")  # si son menores de 7 días imprimimos el mensaje
            else:
                semanas = dias // 7  # calculamos el número de semanas
                dias = dias % 7  # calculamos el número de días restantes
                print(f"{semanas} semanas, {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos")  # imprimimos el mensaje final