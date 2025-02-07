#Cadenas de texto => STRING 

string_1 = 'hola'
string_2= "hola mundoo"
string_3= """hola mundoo"""

print(string_1) 


"""
CADENAS DE TEXTO => strings
"""

string_1 = 'Hola'
string_2 = "Hola"
string_3 = """Hola"""

# Mini ejercicio 
# nombre = 
# apellido = 
# edad = 
# frase = 

'''
# Para obtener datos del usuario 
nombre = input("Escribe tu nombre -> ")
print(type(nombre))
apellido =  input("Escribe tu apellido -> ")
edad =  input("Escribe tu edad -> ")
'''

# METODOS DE LOS STRINGS 
frase = "esto es una frase un poco larga, pero podría serlo más"

# Primer caracter del string  
print("frase[0] ->", frase[0])

# Último caracter del string  
print("frase[-1] ->", frase[-1])

# 6 primeros caracteres  
print("frase[0:6] ->", frase[:6]) # [inicio : fin : paso]

# 6 últimos caracteres  
print("frase[0:6] ->", frase[-6:])

# Caracteres en posición par
print("frase[::2] ->", frase[::2])

# Cuántos caracteres hay en el string 
print("len(frase) ->", len(frase))

# Convertir el texto a mayúsculas
print(frase.upper())
frase = frase.upper()
print(frase)

# Convertir el texto a minúsculas
print(frase.lower())
frase = frase.lower()
print(frase)

# Empezar el string con mayúsculas
print(frase.capitalize())
frase = frase.capitalize()

# Invertir mayúsculas y minúsculas
print(frase.swapcase())

# Contar caracteres (sensible a mayúsculas y minúsculas)
print("frase.count('Es') ->", frase.count("Es"))

# Encontrar la posición de un caracter o grupo de caracteres
print("frase.find('a')", frase.find("a")) # devuelve -1 si no existe ese caracter

# Verificar si el texto empieza por cierto caracter o grupo de caracteres
http = "https://google.com"
print(http.startswith("https"))

# Verificar si el texto acaba por cierto caracter o grupo de caracteres
print(http.endswith(".com"))

# Verificar si el texto es convertible a numero
numero = "10"
print(int(numero))
print(numero.isnumeric()) # solo numeros
print(numero.isalpha()) # solo texto
print(numero.isalnum())

# Cambiar caracteres
print(frase.replace("a", "i"))

palabras_en_frase = frase.split(" ")
print(palabras_en_frase)
print(len(palabras_en_frase))

print( 10 > 5 )
print( "abeja" > "flor")


# Mini ejercicio 
texto = "bUeNos dÍAs" # Buenos días

"""
CADENAS DE TEXTO => strings
"""

string_1 = 'Hola'
string_2 = "Hola"
string_3 = """Hola"""

# Python puede ordenar alfabéticamente
print( 10 > 5 )
print( "abeja" > "flor")

# Mini ejercicio 
# nombre = 
# apellido = 
# edad = 
# frase = 

'''
# Para obtener datos del usuario 
nombre = input("Escribe tu nombre -> ")
print(type(nombre))
apellido =  input("Escribe tu apellido -> ")
edad =  input("Escribe tu edad -> ")
'''

# METODOS DE LOS STRINGS 
frase = "esto es una frase un poco larga, pero podría serlo más"

# Primer caracter del string  
print("frase[0] ->", frase[0])

# Último caracter del string  
print("frase[-1] ->", frase[-1])

# 6 primeros caracteres  
print("frase[0:6] ->", frase[:6]) # [inicio : fin : paso]

# 6 últimos caracteres  
print("frase[0:6] ->", frase[-6:])

# Caracteres en posición par
print("frase[::2] ->", frase[::2])

# Cuántos caracteres hay en el string 
print("len(frase) ->", len(frase))

# Convertir el texto a mayúsculas
print(frase.upper())
frase = frase.upper()
print(frase)

# Convertir el texto a minúsculas
print(frase.lower())
frase = frase.lower()
print(frase)

# Empezar el string con mayúsculas
print(frase.capitalize())
frase = frase.capitalize()

# Invertir mayúsculas y minúsculas
print(frase.swapcase())

# Contar caracteres (sensible a mayúsculas y minúsculas)
print("frase.count('Es') ->", frase.count("Es"))

# Encontrar la posición de un caracter o grupo de caracteres
print("frase.find('a')", frase.find("a")) # devuelve -1 si no existe ese caracter

# Verificar si el texto empieza por cierto caracter o grupo de caracteres
http = "https://google.com"
print(http.startswith("https"))

# Verificar si el texto acaba por cierto caracter o grupo de caracteres
print(http.endswith(".com"))

# Verificar si el texto es convertible a numero
numero = "10"
print(int(numero))
print(numero.isnumeric()) # SOLO NÚMEROS ENTEROS
print(numero.isalpha()) # SOLO LETRAS
print(numero.isalnum()) # NÚMEROS Y LETRAS

# Cambiar caracteres
print(frase.replace("a", "i"))

palabras_en_frase = frase.split(" ")
print(palabras_en_frase)
print(len(palabras_en_frase))

texto_con_espacios = "            Hola que haces       "
texto_sin_espacios = texto_con_espacios.strip()
print("texto_sin_espacios", texto_sin_espacios)




# Mini ejercicio 
texto = "bUeNos dÍAs" # Buenos días
