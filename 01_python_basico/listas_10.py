# LISTAS 

#las listas equivalen a los "arrays" de otros lenguajes 
# las listas y los string son "iterables" 
#la separacion de elementos se realiza mediante comas,
# el indice comienza a contar desde 0
# las listas se indican mediantes corchetes [ ]


lista_numeros = [1,2,3,4,5] 
lista = [1, 2, 3, 4, 5] # lista de numeros 
lista_nombres = ["Maria", "Pau", "Pol" ] # es una lista de strings 
lista_mixtas = [1, "hola", 3.5, True ] # lista mixtas 
lista_de_listas = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] # lista de listas

# Acceder al primer valor 
print(lista_numeros[0]) #1 
# Acceder al ultimo valor 
print(lista_numeros[-1]) #5 
#SLICING ( atencion: el ultimo valor no esta incluido)
#[ inicio : final : paso ]
print(lista_numeros[1:3]) # [2,3]
print(lista_numeros[-3:-1]) # [3,4] 
print(lista_numeros[::1]) # [5,4,3,2,1]
print(lista_numeros) # [1,2,3,4,5] 


#Añadir un elemento al final

lista_numeros.append(6)  
print(lista_numeros) # [1,2,3,4,5,6]

#Quitar un elemento al final 
ultimo_numero = lista_numeros.pop() #nombre_lista.pop() 

#Poner un elemento en una posicion especifica 
lista_numeros.insert(2, 3) # posision y valor
print(lista_numeros) 


# eliminar un elemento por valor
print(lista_nombres)
lista_nombres.remove("Pol")
print(lista_nombres)


#eliminar por una posicion concreta -> del [ posicion ] 

print(lista_mixtas) 
del lista_mixtas[2]
print(lista_mixtas)

#Unir dos listas 

lista_1 = [0,1,2]
lista_2 = [3,4,5]

lista_1.extend(lista_2)
print(lista_1) 


#concatenar Listas 
lista_1.extend(lista_2)
lista_1 = lista_1 + lista_2
lista_1 += lista_2



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