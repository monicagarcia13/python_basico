# OPERADORES LOGICOS 
#Sirven para poder cambiar diversas condiciones 

#and -> y 

print("True and true", True and True) # True
print("True and false", True and False) # False
print("False and true", False and True) # False
print("False and false", False and False) # False

# or -> 0
print("True or True  ->" , True or True) #True
print("False and True ->", False or True) #True
print("False or False ->", False or False) #false 








## Operadores lógicos (and, or, not)
edad = 17
tramite = edad >= 18 and edad <= 65 ## Devuelve True si cumplimos las las 2 condiciones dadas
semaforo = "Rojo"
cruzar = semaforo == "Verde" or semaforo == "Amarillo" # Devuelve True si cumplimos al menos una de las dos condiciones
verdad = True
negacion = not verdad # Niega la estructura siguiente

## Operadores de identidad (is, is not)
nombre = "Sergie Code"
profesor = "Sergie Code"
alumno = "Pedrito"
sonElMismo = nombre is profesor # Nos devuelve True si son iguales
sonDistintos = profesor is not alumno # Nos devuelve True si son distintos

## Operadores de pertencia (in, not in)
palabra = "Mundo"
palabra2 = "Mercurio"
texto = "Hola Mundo"
pertenece = palabra in texto # Nos devuelve True si pertenece
noPertenece = palabra2 not in texto # Nos devuelve True si no está presente

"""
OPERADORES LÓGICOS
Sirven para poder combinar diversas condiciones
"""

# and -> y JS -> &&
print("True and True -> ", True and True) # True
print("True and False ->", True and False) # False
print("False and False -> ", False and False) # False

# or -> o JS -> ||
print("True or True -> ", True or True) # True
print("False or True -> ", False or True) # True
print("False or False -> ", False or False) # False

# not -> no JS -> !
print("not True -> ", not True) # False