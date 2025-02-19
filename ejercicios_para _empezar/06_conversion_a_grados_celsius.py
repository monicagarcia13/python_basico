'''
EJERCICIO 6: CONVERSIÓN A GRADOS CELSIUS
Haz un programa que pida al usuario la temperatura en grados Fahrenheit
La respuesta del programa será:
"X grados Fahrenheit equivalen a Y grados Celsius" (los valores que sean)
Formúla de conversión : Fahrenheit = (Celsius * 9/5) + 32
'''

while True:
    try:
        fahnrenheit = float(input("Bienviendo!, Introduce la temperatura en grados Fahrenheit => "))
        break
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")

celsius = (fahnrenheit - 32) * 5 / 9
celsius_redondeado = round(celsius, 2)
resultado = f"{fahnrenheit} grados Fahrenheit equivalen a {celsius_redondeado} grados Celsius"
print(resultado)