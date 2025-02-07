"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 2a

Mostraremos el texto: "Contar letras en un texto"

Pediremos al usuario un texto, así:
"Por favor, introduzca un texto "
Puede contener números y caracteres con tilde.

A continuación mostraremos las letras que contiene y cuantas son,
ordenadas por número de apariciones. En caso de empate, en orden alfabético. 
Ignoraremos los números, los espacios y los signos de puntuación 
(punto, coma, punto y coma, exclamación, etc.)
Consideremos mayúsculas y minúsculas como la misma letra.

Por ejemplo:
"Por favor, introduzca un texto " ¿Amar?
La respuesta sería: 
"El texto contiene las letras:
a, 2 veces
m, 1 vez
r, 1 vez
"

Por ejemplo:
"Por favor, introduzca un texto " Python forever and ever
La respuesta sería: 
"El texto contiene las letras:
e, 4 veces
r, 3 veces
o, 2 veces
n, 2 veces
a, 1 vez
f, 1 vez
h, 1 vez
p, 1 vez
v, 1 vez
y, 1 vez
"

# Ejercicio 2b

# Mostraremos el texto: "Contar palabras en un texto"
# Lo mismo que el ejercicio anterior, pero con palabras en lugar de letras.
# . 
# """


# ejericio 1 

print("Contar letras en un texto") # imprimimos el texto 
texto = input("Por favor, introduzca un texto: ").lower() # pedimos al usuario que introduzca un texto y lo convertimos a minúsculas 

letras = {} # creamos un diccionario para contar las letras
for letra in texto: # iteramos sobre cada letra del texto
    if letra.isalpha():  # Solo cuenta letras, ignora números y signos
        letras[letra] = letras.get(letra, 0) + 1 # si es una letra,  el get obtiene el valor de la letra 
        #sumamos 1 a la cantidad de veces que aparece y el get devuelve el valor por defecto 0

# Ordenamos por cantidad y luego alfabéticamente
letras_ordenadas = sorted(letras.items(), key=lambda x: (-x[1], x[0])) # el lambda es una función anónima en python
# (-x[1] este codigo es la cantidad de veces que aparece la letra y x[0] es el letra)
# el key es funcion que se utiliza par extraer un valor 

print("El texto contiene las letras:") # imprimimos el texto 
for letra, cantidad in letras_ordenadas: # iteramos sobre cada letra y su cantidad
    print(f"{letra}, {cantidad} {'veces' if cantidad > 1 else 'vez'}") # imprimimos el letra, la cantidad y si es más de 1 imprimimos vez

# ejercicio 2 


print("Contar palabras en un texto") # imprimimos el texto 
texto = input("Por favor, introduzca un texto: ").lower() # pedimos al usuario que introduzca un texto y lo convertimos a minúsculas

# Reemplazamos signos de puntuación con espacios
for signo in ".,;!?¿¡": 
    texto = texto.replace(signo, " ") # el replace reemplaza los signos de puntuación por espacios

palabras = texto.split()  # Separa el texto en palabras
conteo = {} # creamos un diccionario para contar las palabras

for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1 #si es una palabra sumamos 1 a la cantidad 
    #de veces que aparece y el get devuelve el valor por defecto 0
    # el get obtiene un valor 

# Ordenamos por cantidad y luego alfabéticamente
palabras_ordenadas = sorted(conteo.items(), key=lambda x: (-x[1], x[0])) # el lambda es una función anónima que
#toma un argumento x y devuelve un tupla de dos elementos y el sorted ordena 

print("El texto contiene las palabras:")
for palabra, cantidad in palabras_ordenadas:
    print(f"{palabra}, {cantidad} {'veces' if cantidad > 1 else 'vez'}")
