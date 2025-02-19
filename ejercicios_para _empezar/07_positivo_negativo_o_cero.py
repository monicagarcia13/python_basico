'''
EJERCICIO 7: POSITIVO, NEGATIVO O CERO
Haz un programa que pida al usuario un número y diga si es positivo, 
negativo o cero
'''

while True:
    try:
        numero = int(input("Introdue un numero => "))
        break
    except ValueError:
        print("Numero incorrecto. Por favor, introduce un número")

if numero > 0:
    print(f"{numero} es positivo")
elif numero < 0:
    print(f"{numero} es negativo")
else:
    print(f"{numero} es cero") 
exit()




