# Tenemos esta lista de animales:
# ["gato", "perro", "caballo", "paloma", "murcielago", "leon", "mono"]

# Vamos a pedir una letra al usuario y mostraremos los animales que contienen esa letra.
# Si no hay ninguno diremos "Ningún animal contiene esa letra"

letra = input("Escribe una letra -> ") # pedimos una letra al usuario
lista_animales = ["gato", "perro", "caballo", "paloma", "murcielago", "leon", "mono"] 
animales  =  []  # creamos una lista vacía
for animal in lista_animales: # recorremos la lista de animales
    if letra in animal: # si la letra está en el animal
        animales.append(animal) # lo añadimos a la lista de animales
print(f"Los animales que contienen la letra {letra} son: {animales}") # imprimimos la lista de animales
if not animales: # si la letra no está en ningún animal, imprimimos "Ningún animal contiene esa letra"
    print("Ningún animal contiene esa letra")