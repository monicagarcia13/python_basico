"""
EJERCICIO 5 : CONVERSIÓN A KM
Haz un programa que haga lo opuesto a lo anterior,
convertir millas es kilómetros
"""

Millas_a_km = 1 / 0.621371  # 1 km es aproximadamente 1.60934 millas

while True:
    try:
        millas = float(input("Bienvenido \nIntroduce la distancia a convertir en km => "))
        break
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")

kilometros = millas * Millas_a_km
kilometros_redondeados = round(kilometros, 2)
resultado = f"{millas} millas equivalen a {kilometros_redondeados} km"
print(resultado)
