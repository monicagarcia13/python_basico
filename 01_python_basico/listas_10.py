"""
LISTAS
"""


# REPASO DE LISTAS 

# Lista vacia 
lista = []

lista.append("Ana")
print(lista) # Ana

#Las listas son colecciones de datos indexados 
# el indice empienza por  
lista[0]

Lista_enteros = list(range(1,21,2))
print(Lista_enteros)


lista_nombres = ["Pol", "Noa", "Sara", "Pepe" ]

for nombre in lista_nombres:
    indice = lista_nombres.index(nombre)
    print(f"{indice} . {nombre}")

for indice, valor in enumerate(lista_nombres): 
    print(f"{indice} . {valor}")


# Copia de una lista ( copy )

nueva_lista1 = lista_nombres.copy()
nueva_lista2 = lista_nombres[:] 


#Mini ejercicio #Obtener los numeros elevados al cuadrado de la serie 

lista_numeros = list(range(0,11))

# necesitamos otra lista solo con los numeros elevados al cuadrado de la lista_numeros 

lista_numeros_cuadrados = [x**2 for x in lista_numeros]
print(lista_numeros_cuadrados)


# esto es la desestruturacion de una lista
#y obtener el valor de una lista 

lista_ciudades = [ 'NY', 'LA', 'BCN']
ny, la, bcn = lista_ciudades 
print(bcn)
 
 











# Las listas equivalen a los "arrays" de otros lenguajes
# Las listas se indican mediante corchetes -> []
# Las listas y los string son "iterables"
# La separación de elementos se realiza mediaante comas
# La lista es una colección (de datos) indexada
# El índice empieza a contar desde 0

verdadero = True
lista_numeros= [1, 2, 4, 5] # lista de números enteros
lista_nombres = ["Pol", "Maria", "Pau", "Pol"] # lista de strings
lista_mixtas = [1, "hola", 3.5, True] # lista mixtas
lista_de_listas = [[1, 2], [3, 4], [5, 6]] # lista

# Acceder al primer valor:
print(lista_numeros[0]) # 1
# Acceder al último valor:
print(lista_numeros[-1]) # 5 
# SLICING (atención el último valor no está incluido)
# [inicio : final : paso]
print(lista_numeros[1:3]) # [2, 3]
print(lista_numeros[-3:-1]) 
print(lista_numeros[-3:]) # [3, 4, 5]
print(lista_numeros[::-1]) # [5, 4, 3, 2, 1]
print(lista_numeros) # [1, 2, 3, 4, 5]

# Añadir un elemento al final
lista_numeros.append(6) # nombre_lista.append(valor)
print(lista_numeros) # [1, 2, 4, 5, 6]

# Quitar el último elemento
ultimo_numero = lista_numeros.pop() # nombre_lista.pop()

# Poner un elemento en una posición concreta
lista_numeros.insert(2, 3) # nombre_lista.insert(posición, valor)
print(lista_numeros)
 
# Eliminar por una posición concreta --> del[posicion]
print(lista_mixtas)
del lista_mixtas[2]
print(lista_mixtas)

# Eliminar un elemento por valor
print(lista_nombres)
lista_nombres.remove("Pol")
print(lista_nombres)

lista_1 = [0, 1, 2]
lista_2 = [3, 4, 5]

# Concatenar listas
# lista_1.extend(lista_2)
# lista_1 = lista_1 + lista_2
lista_1 += lista_2


print(lista_1)






### Ejemplos de listas en Python:


# ### Métodos comunes de las listas:
# - `append(x)`: Añade un elemento al final de la lista.
# - `insert(i, x)`: Inserta un elemento en la posición especificada.
# - `remove(x)`: Elimina la primera aparición del elemento especificado.
# - `pop([i])`: Elimina y devuelve el elemento en la posición especificada. Si no se especifica la posición, elimina y devuelve el último elemento.
# - `clear()`: Elimina todos los elementos de la lista.
# - `index(x)`: Devuelve el índice de la primera aparición del elemento especificado.
# - `count(x)`: Devuelve el número de veces que el elemento especificado aparece en la lista.
# - `sort()`: Ordena los elementos de la lista.
# - `reverse()`: Invierte el orden de los elementos de la lista.

# Las listas son una herramienta fundamental en Python y se utilizan ampliamente para almacenar y manipular colecciones de datos.