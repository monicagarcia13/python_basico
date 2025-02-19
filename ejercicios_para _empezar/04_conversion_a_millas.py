"""
EJERCICIO 4 : CONVERSIÓN A MILLAS
Haz un programa que pida al usuario la distancia a convertir (en km)
Redondea el resultado a dos decimales
La respuesta del programa será:
"X km equivalen a Y millas" (los valores que sean)
Nota: 1 km son 0.621371 millas
"""

Km_millas = 0.621371


distancia_km = float(input("Introduce la distancia a convertir (en km) => "))

millas = distancia_km * Km_millas

millas_rendondeada = round(millas,2)
resultado = f"{distancia_km} km equivalen a {millas_rendondeada} millas"
print(resultado)

while input("¿Quieres volver a preguntar o salir? (s/n)").lower() == "s":
    distancia_km = float(input("Introduce la distancia a convertir (en km) => "))
    millas = distancia_km * Km_millas
    millas_rendondeada = round(millas, 2)
    resultado = f"{distancia_km} km equivalen a {millas_rendondeada} millas"
    print(resultado)
    
print("¡Adiós!")