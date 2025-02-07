"""
PROPIEDADES DE LO NÚMEROS
"""
"""
PROPIEDADES DE LO NÚMEROS
"""

# OPERACIONES MATEMÀTICAS
suma =  1 + 3
resta = 1 - 4
multiplicacion = 4 * 2
division = 10 / 2
exponencial = 2 ** 3
exponencial = 4 ** 0.5
division_entera = 20 // 6
modulo = 20 % 3
modulo = 78889900000343637378 % 2

# Precedencia de las operaciones -> pon paréntesis 
operacion = (1 + 2) - (3 * (4 / 5) )

tipo = type(operacion)
print(tipo)

print(type(operacion))


# OPERACIONES DE COMPARACIÓN
# El resultado de una comparación SIEMPRE es un booleano 

# comparar si dos números son iguales
comparacion_1 = 1 == 2
print(comparacion_1)

# comparar si dos números son diferentes
comparacion_2 = 1 != 2
print(comparacion_2)

# comparar si un número es mayor que otro
print( 1 > 2) # False
print( 1 > 1) # False
print( 1 >= 1) # True

# comparar si un número es menor que otro
print( 1 < 2) # False
print( 1 < 1) # False
print( 1 <= 1) # True

verdadero = True
# True = False # Error crítico de sintaxis
print( "True es", True )

# MÉTODOS PARA NÚMEROS 
# redondear un número a la izquierda o derecha
redondear_izquierda = round(3.14159265359, 2) # valor a redondear, número de decimales

# Valor absoluto
valor_absoluto = abs(-5) # 5


# OPERACIONES MATEMÀTICAS
suma =  1 + 3
resta = 1 - 4
multiplicacion = 4 * 2
division = 10 / 2
exponencial = 2 ** 3
exponencial = 4 ** 0.5
division_entera = 20 // 6
modulo = 20 % 3
modulo = 78889900000343637378 % 2

# Precedencia de las operaciones -> pon paréntesis 
operacion = (1 + 2) - (3 * (4 / 5) )

tipo = type(operacion)
print(tipo)

print(type(operacion))


# OPERACIONES DE COMPARACIÓN
# El resultado de una comparación SIEMPRE es un booleano 

# comparar si dos números son iguales
comparacion_1 = 1 == 2
print(comparacion_1)

# comparar si dos números son diferentes
comparacion_2 = 1 != 2
print(comparacion_2)

# comparar si un número es mayor que otro
print( 1 > 2) # False
print( 1 > 1) # False
print( 1 >= 1) # True

# comparar si un número es menor que otro
print( 1 < 2) # False
print( 1 < 1) # False
print( 1 <= 1) # True

verdadero = True
# True = False # Error crítico de sintaxis
print( "True es", True )

#METODOS PARA NUMEROS 
#rendondear un numero a la izquierda o derecha


redondear_izquierda = round(3.14159, 2)  #Valor
"Propiedades de los numeros" 

#Operaciones matematica con numeros 
    
    # Suma
    #a = 1 + 2 
    #ivisión
d = 1 / 2 
print(d)
    
    # Modulo
e = 1 % 2 
print(e)
    
    # Exponente
f = 1 ** 2 
print(f)
    
    # División entera
g = 1 // 2 
print(g)
    
    # División de enteros
h = 1 / 2
print(h)
    
    # División de enteros
i = 1 // 2
print(i)
    
# División de enteros
j = 1 % 2
print(j)
    
# División de enteros
k = 1 ** 2
print(k)

operacion = (1 + 2) - (3 * (4  / 5) )
print(operacion)


#Operaciones de comparacion 

# comparar si dos numeros son iguales 
comparacion_1= 1 == 2 
print(comparacion_1)

#comparar si dos numeros son diferentes
comparacion_2= 1 != 2 
print(comparacion_2)

#comparar si un numero es mayor que otro
print( 1 > 2) #false
print( 1 > 1) #false
print( 1 >= 1) #true

# comparar si un numero es menor que otro
print(1 < 2) #true
print( 1 < 1) #false


#


mi_nombre = 'Monica'
mi_apellido = 'Garcia'
mi_edad = 27
resultado = "Mi nombre es " + mi_nombre + " y mi apellido es " + mi_apellido + " y tengo " + str(mi_edad) + " años"
resultado = f"Mi nombre es {mi_nombre} y mi apellido es {mi_apellido} y tengo {mi_edad} años"

print(resultado)

#colocar str y f para concatenar ç

#input siempre devuelve un string

#Para obtener datos del usuario 

nombre = input("Escribe tu nombre -> ")
print(type(nombre)) 
apellido = input("Escribe tu apellido -> ")
print(type(apellido))

#Metodos  de los string

frase = "esto es una frase"


# Primer careacter del string
print("frase[0] -> " + frase[0])

#ultimo caracter del string

print("frase[-1] -> " + frase[-1])

# 6 primeros caracteres 

print("frase[0:6] -> " + frase[0:6])

# 6 ultimos caracteres 
print("frase[0:6] ->", frase[-6:])

#caracteres en posicion par 
print("frase[0:6] ->", frase [::2])

#cuantos carecteres  hay en el string

print("len(frase) ->", len(frase))

#Convertir el texto en mayusculas 

print(frase.upper())
frase = frase.upper() 
print(frase)

#Convertir el texto en minisculas 

print(frase.lower())
frase = frase.lower() 
print(frase)


#empezar el string en una posicion determinada
print(frase.capitalize)
frase = frase.capitalize()

# invertir  mayusculas y minisculas 
print(frase.swapcase())

#contar caractares 

print("frase.count('a') ->", frase.count("a"))

#encontrar la posicion de un caracter o grupos de caracteres 

print("frase.find('a')", frase.find("a")) #devuelve -01 si no existe ese caracter 

#verificar si el texto empienza por ciert caracter o grupo de caracteres 
frase = "Aprendiendo python"
print(frase.startswith('https')) 
#devuelve true

#verificar si el texto acaba por cierto caracter o grupo de caracteres 
print(frase.endswith(".com")) 

#verificar si el texto se covierte a numero 
numero = "10" 
print(int(numero)) 
print(numero.isnumeric()) # solo numeros
print(numero.isalpha()) # solo texto
print(numero.isalnum()) 

#cambiar caracteres 
print(frase.replace("aprendiendo", "aprendiendo python"))

palabras_en_frase = frase.split() 
print(len(palabras_en_frase)) 


#Mini ejercicio 

texto = "bUeNos dIas" 
texto = texto.capitalize() 
print(texto)



