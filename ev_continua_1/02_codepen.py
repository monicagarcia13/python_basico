# '''
# Vamos a recibir un texto por parte del usuario.
# Con ese texto vamos a generar otro sin las vocales ni los espacios
# '''

# texto = input("escribe un texto -> ").lower()

# exclusiones = "aeiou á"
# exclusiones = ["a", "e", "i", "o", "u", " ", "á"]

# for caracter in exclusiones:
#     texto = texto.replace(caracter, "")

# print(texto)


texto = input("Escribe un texto -> ") # pedimos un texto al usuario
vocales = "aeiouAEIOU"  # Definimos las vocales que queremos eliminar

resultado = "".join(letra for letra in texto if letra not in vocales and letra != " ")
# recorremos cada letra del texto, y el join nos devuelve un texto con las vocales eliminadas 

print("Texto sin vocales ni espacios:", resultado)  