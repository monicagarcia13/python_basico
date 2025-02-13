"""
REPASO LISTAS
Es una colección MUTABLE de datos
"""

# lista vacía
lista = []

lista.append("Anna")
print(lista) # ["Anna"]
lista[0] = "Marta"
print(lista)

# Las listas on colecciones de datos indexados
# el índice empieza en 0
lista[0]

lista_enteros = list(range(1,21,2))
print(lista_enteros)

lista_nombres = ["Pol", "Noa", "Sara", "Pepe"]
#      indices --> 0      1       2       3

for nombre in lista_nombres:
    indice = lista_nombres.index(nombre)
    print(f"{indice}. {nombre}")

for indice, valor in enumerate(lista_nombres):
    print(f"{indice}. {valor}")

# Copia de una lista
nueva_lista_1 = lista_nombres.copy()
nueva_lista_2 = lista_nombres[:]

# Mini ejercicio: obtener los números elevados al cuadrado de la serie
lista_numeros = list(range(0, 11)) # Hay que obtener --> 0, 1, 4, 9, ...
print(lista_numeros)

# Necesitamos otra lista sólo con los números elevados al cuadrado de lista_numeros
# Forma 1 --> súper básica
lista_cuadrados = []
for numero in lista_numeros:
    lista_cuadrados.append(numero**2)
print(lista_cuadrados)

# Forma 2 --> List comprehensions
lista_cuadrados  = print([ numero**2 for numero in lista_numeros ])

lista_ciudades = ['NY', "LA", "BCN"]
ny, la, bcn = lista_ciudades
print(bcn)




# for index, valor in enumerate(lista_numeros):
#     lista_numeros[index] = index+100

# print(lista_numeros)





 


