""""
PALÍNDROMOS
Son textos iguales de derecha a izquierda que de izquierda a derechacios 
Se ignoran los espacios, los signos de puntuación y las mayúsculas.
"""
import os
os.system("cls")

frase = "Amor a Roma"
frase = "Viernes"
frase = "Dabale arroz a la zorra el abad"

# Ponemos la frase en minúsculas
frase = frase.strip().lower()
# Eliminamos los espacios
palabras_frase = frase.split()
# Volvemos a generar la frase sin espacios
palabras_frase = "".join(palabras_frase)
print(palabras_frase)

# Inverimos la frase
frase_invertida = frase[::-1]
# Eliminamos los espacios
palabras_frase_invertida = frase_invertida.split()
# Volvemos a generar la frase sin espacios
palabras_frase_invertida = "".join(palabras_frase_invertida)
print(palabras_frase_invertida)

if palabras_frase == palabras_frase_invertida:
    print("La frase es un palíndromo")
else:
    print("La frase no es un palíndromo")
