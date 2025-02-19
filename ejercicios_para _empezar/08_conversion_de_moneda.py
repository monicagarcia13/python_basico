# '''
# EJERCICIO 8: CONVERSIÓN DE MONEDAS
# Haz un programa que pida al usuario la cantidad de euros que quiere convertir a dólares
# La respuesta del programa será:
# "X euros equivalen a Y dólares" (los valores que sean)
# Formúla de conversión : 1 euro = 1.18 dólares

# '''

while True:
    try:
        euros = int(input("Introduce la cantidad de euros que quiere convertir a dolares =>"))
    except ValueError:
        print("Numero invalido, por favor intruzca una cantidad correcta")

    dolares = euros * 1.18
    dolares_redondeados = round(dolares, 2)
    resultado = f"{euros} euros equivalen a {dolares_redondeados} dolares"
    print(resultado)
    if input("¿Quieres volver a preguntar o salir? (s/n)").lower() != "s":
        break
    

# Conversión de euros a dólares
euros = float(input("Introduce la cantidad de euros a convertir: "))
dolares = euros * 1.18
print(f"{euros} euros equivalen a {dolares:.2f} dólares")

# Función para convertir euros a dólares

def convertir_euros_a_dolares(euros):
    return euros * 1.18

euros = float(input("Introduce la cantidad de euros a convertir: "))
dolares = convertir_euros_a_dolares(euros)
print(f"{euros} euros equivalen a {dolares:.2f} dólares")

# Función para convertir euros a dólares con mensaje

def conversion():
    euros = float(input("Introduce la cantidad de euros a convertir: "))
    print(f"{euros} euros equivalen a {euros * 1.18:.2f} dólares")

conversion()


