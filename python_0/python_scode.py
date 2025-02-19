
"""

Python es un lenguaje de programación interpretado, orientado a objetos, de tipado dinámico y de alto nivel.
Fue creado por Guido van Rossum y liberado en 1991.
Es multiplataforma y tiene una gran comunidad de desarrolladores.

se puede usar para crear aplicaciones, juegos y programas de computadoras.
ciencia de datos, inteligencia artificial, web scraping, automatización de tareas, desarrollo de aplicaciones web, etc.

desarrollo de sotware: 
 Para que sirve python ? -- > 

    - desarrollo de aplicaciones
    - automatización de tareas
    - web scraping ( extraccion de datos , se analizan y se hace la interfaz de usuario)
    - desarrollo de aplicaciones web
    - desarrollo de juegos
    - inteligencia artificial
    - ciencia de datos
    -aplicaciones de escritorio- PyQt y Kivy, 
    - administración de sistemas 
    - internet de las cosas ( IOT) ( distinto dispositivos que tenga acceso a internet para desarrollar un software)

    """
"""
se puede tambien usar powershell para ejecutar python, y tambien desde un bloc de notas 



"""

print("Hola, mundo") 

if  5 > 3: # if es una palabra reservada , estamos utilizando una condicion 
    print("5 es mayor que 3") 
    # identacion , es importante en python , se usa para definir bloques de codigo osea la sangria 
    # son los espacios, tabulaciones o saltos de linea que se utilizan para organizar el codigo

if 5 > 3: 
    if 5 < 4:
      print("5 es mayor   que 3 y 5 es menor que 4")

# comentarios : se utiliza el # para comentar el codigo, los comentarios no salen en consola 


if 5 > 3: 
   # este comentario esta dentro de una estructura
    print("5 es mayor que 3")   
    # otro comentario 


# comentarios multilinea
# este 
#          es
#                   un
#                      comentario 
# multilinea

"""
hacer 
un 
comentario
multilinea

"""

# variables: 
# es un contenedor para almacenar valores de datos
# este contenedor va a tener un nombre
# es creada la primera vez que se le asgina un valor



x = 5 # x es una variable y 5 es el valor que se le asigna a x
txt = "Esto es un texto" 
print(x) # imprimimos el valor de x
print(txt) # imprimimos el valor de txt

# python es caseSenstive ( interpreta el texto como si fuera mayusculas o minusculas)

# NOMBRES ADMITIDOS DE VARIABLES 

#1. Puede empezar con una letra o un un guion bajo ( underscore)
mivariable = "texto"
_miVariable = 'Otro texto' 

#2. No se puede iniciar con un numier
## 5variable = 'texto

#3. Solo se pueden contener alfanumericos y guiones bajos (A-z, 0-9, y _)
miVariable = "texto"
_123miVariable = "texto"

#4. CaseSensitibe ( no solo al comienzo si no en general)

#5. no se puede utilizar palabras reservadas de python ( Keywords)

###########

#Convenciones de esctrictura de variables 

#CamelCase 
camelCase = " Comienza con minúsculas y cada palabra siguiente con mayusculas"

#PascalCase
PascalCase = " Comienza con mayusculas y cada palabra siguiente con mayusculas"

#snake_case

snake_case = " todas las palabras en minusculas y separadas por guiones bajos"

#######

# Multiasignacion

x, y, z = "Naranja", "Banana", "Cereza"
print(x)
print(y)
print(z)

a = b = c = "Monica"
print(a)
print(b)
print(c)



# multiasignacion desde colecciones 

frutas = ["naranja", "pera"  , "lima"]
n,p,l, = frutas

print(n)
print(p)
print(l)

# uso de print y salidas 

txt = "Curso"
text2 = "de"
text3 = "python"

print(txt , text2 ,text3)

# con el signo + concatenar
# con la , te da un espacio entre cada elemento

# Variables globales versus variables de Scope 

variableGlobal = "Esta variable estara disponible para todo el  programa" 

def funcion(): 
    variableScope = "Esta variable solo estara solo dispoible dentro de la funcion"
    print(variableGlobal)
    print(variableScope)
    
funcion() 

# con global la variable estara disponible para todo el programa 

########################

#TIPOS DE DATOS 

#1. str ( string ) Texto o cadena de caracteres
comillasSimples = 'Hola'
comillasDobles = "Hola"
comillasTriples = """Hola"""
comillasTriplesSimples = '''Hola'''


#2. int ( integer) numero entero 
numero_entero = 5 

#3. float ( float) numero decimal
numero_decimal = 3.14

#complex ( complex) numero complejo  parte entera y otra parte imaginaria) 
numero_complejo = 3 + 4j

# list []: Coleccion ordenada y mutable de elementos ( cada elementos tendra un indice) 
lista =  [0,1,2,3,4,5,5,5]
print(lista)

#tupla(): Coleccion ordenada y immutable de elementos ( cada elementos tendra un indice) 
tupla = (0,1,2,3,4,5)
tupla = ("a," "b", "c")

#range: es una secuencia de numeros generada dentro de un rango
rango = range(1,10) # genera numeros de 1 a 9

# dic ( dictionary){} Coleccion de pares clave-valor(key-value) desordenada y mutable 
diccionario = {"nombre": "Monica Garcia", }

#set {} coleccion desordenada de elementos unicos y mutables 
conjunto = {1,1,2,2,3}
print(conjunto)

#frozenset([]) coleccion desordenada de elementos unicos e inmutables
conjunto_immutable = frozenset([1,1,2,2,3])

#boleanos ( booleans) True o False
boleanoVerdadero = True
boleanoFalse = False

###########

#TIPOS DE DATOS NUMBERS


#2. int ( integer) numero entero 
numero_entero = 5 

#3. float ( float) numero decimal
numero_decimal = 3.14

#complex ( complex) numero complejo  parte entera y otra parte imaginaria) 
numero_complejo = 3 + 4j

# print(numero_entero)
# print(type(numero_entero))

# print(numero_decimal)
# print(type(numero_decimal))

# print(numero_complejo)
# print(type(numero_complejo))


#CASTEO

decimal_desde_entero = float(numero_entero)
entero_desde_decimal = int(numero_decimal)
complejo_desde_entero = complex(numero_entero)
complejo_desde_decimal = complex(numero_decimal)


print(decimal_desde_entero)
print(entero_desde_decimal)
print(complejo_desde_entero)
print(complejo_desde_decimal)


##### RANDOM

import random

aleatorio = random.randrange(1,10) # el numero de stop no es excluyente
print(aleatorio)

aleatorio_par = random.randrange(2,11,2) # numero par del 2 a 10 incluido
print(aleatorio_par)


aleatorio_impar = random.randrange(1,10,2) # numero impar del 1 a 9 incluido 
print(aleatorio_impar)

#####  STRINGS (CADENA DE TEXTO )

text = "Estoy viendo una pelicula"

#1. str ( string ) Texto o cadena de caracteres
comillasSimples = 'Hola'
comillasDobles = "Hola"
comillasTriples = """Hola"""
comillasTriplesSimples = '''Hola'''


##### Listas o arrays de caracteres

texto = "Este es un curso de Python por Sergie Code" # podemos seleccoonar un caracter por indice 
caracter =texto[5]
print(caracter)

# len ( length ) Saber el numero de caracteres en una cadena
amplitud = len(texto)
print(amplitud)

# In: para saber si esta incluido en el texto
print("PeliCula".lower() in texto.lower()) # devuelve un boleano

# Not in: con la palabra reservada not podemos negar y pedir un resultado negativo 
print("serie" not in texto) # devuelve un True o False segun corresponda 

# Slice ( cortar ) # una parte del texto 
print(texto[10:17]) # Se imprimira el fragmento que vaya desdee el indice 10 al 16 (no incluido) 
print(texto[:5]) # se imprimiera el fragmento que se vaya desde el comineoz hasta el indice 5 (no incluido)
print(texto[38:]) # se imprimira el fragmento que se vaya desde el indice 38 hasta el final del texto (incluido)
print(texto[-4:]) # se imprimira el fragmento que se vaya desde el final del texto hasta el indice 4 (incluido)
print(texto[37:])

#Modificadores de texto ( mayusuculas, minusculas, etc) 

mayusculas = "Este es un curso de Python por Sergie Code"
# el split eliminara los espacios del comienzo y el final 
# reemplazo - > el replace reemplazara una cadena por otra


texto_con_comas = "Tengo, que, aprender, a ,programar, en, Python"
seperar_por_comas = texto_con_comas.split(",")
print(seperar_por_comas) # devolera una lista 

mayusculas = texto.upper() # se cambia a mayusculas
print(mayusculas)

minusculas = texto.lower() # se cambia a minusculas
print(minusculas)

## METODOS MAS USADOS 
 # el capitalize cambia a mayusculas la primera letra de cada palabra
 #el startswith verifica si el texto comienza con una palabra especificada
 #el endswith verifica si el texto termina con una palabra especificada
# si queremos cada palabra a  mayusculas utlizamos el title
# el count devuelve el numero de veces que aparece una palabra en una cadena
# el find  nos devuelve nos el indice donde comienza la palabra buscada 



# F- STRINGS  ( template  strings)
num = 5
nombre = "Pedro"
variable = "edad"
txt = f"la {variable} de {nombre} es {num}" 
print(txt)

# Escapes \ (backslash) - barra invertida
escape = "Mi pais favorito es \"Colombia\" y vivo en España"
print(escape)

# con \\ se puede insertar una barra invertida
#con \n se puede insertar un salto de linea

### BOLEANOS Y OPERADORES 

### Tipo de dato que toma dos valores Verdadero o Falso (True o False)

a = True
b = False

### Nos ayudarán a tomar decisiones

### Estructuras que devuelven verdadero (las que tienen contenido)
string = bool("No se olviden de suscribirse al canal")
num = bool(2022)
lista = bool(['Naranja', 'Manzana'])
dict = bool({"nombre": "Sergie Code"})

### Estructuras que devuelven falso (todas están vacías de contenido)
string2 = bool("")
num2 = bool(0)
lista2 = bool([])
dict2 = bool({})
none = bool(None) # None es un valor que no existe

# OPERADORES 

## Operadores arimeticos (+,-,*,/,%,**,//)

a = 10
b = 5

suma = a + b
print(suma)


# CONDICIONALES IF ELSE.. 

# es la estructura que nos permite tomar un flujo u otroo segun una condicion 

a = 5
b = 9
c = 7 

# la palabra reservada if es obligatoria  en la estructurra pero el elif y el ese son opcionales 

if a > b:  # si cumple esta condicion hace 
    print(f"{a} es mayor que {b}")  # estas lineas de codigo 

elif c > b:  # si no cumple la primera condicion pero cumple esta realiza 
    print(f"{c} es mayor que {b}") # estas otras lineas de codigo 
else: # si no cumple ninguna de las condiciones
    print(f"{a} es menor que {b} y {c} es menos que {b}")  # realiza estas ultimas lineas de codigo 


#ejemplo 

edad = 62

if edad >= 18 and edad <= 60:
    print("Puedes entrar al boliche")
else:
    if edad <= 18:
        print("No tienes la edad para entrar al boliche")
    else:
        print("Este boliche solo es para adultos")

## SHORTHANDS

a = 5
b = 2

if a > b: print("{a} es mayor que {b}")

# BUCLE: estructura que se repite mientras la condicion sea verdadera
#BUCLE WHILE 

## EJEMPLO PRACTICO

# while True:
#     print("No te olvides de suscribirte a mi canal @sergiecode")
#     respuesta = input("¿Desea salir? (s/n)").strip().lower()
#     if respuesta == 's':
#         break

# BUCLE FOR 

lenguajes = ["Python", "JavaScript", "Java", "C#", "Angular", "React", "NodeJs", "Ruby", "Django" ] # esto es una lista 
x = 1

# for lenguaje in lenguajes: # se ejecutara una vez por cada elemento de la lista
#     if lenguaje == "Angular":
#         continue

#     print(f"{x}. {lenguaje}")
#     x += 1
  

texto = " Yo estoy enamorado de una mujer hermosa"
for letra in texto:
    print(letra)

# como iterar una estructura de datos, lista, tupla 

letras = ['a', 'b', 'c']
numeros = [1, 2, 3]

for l in letras:
    for n in numeros:
        print(l,n)


# LISTAS = es una coleccion  ( array )de datos que permite almacenar multiples elementos 
# en una sola variable 

# caracteristicas = ordenada, ( podemos ingresar a un elemento por indice ) y es mutable 
              # 0        # 1       # 2       # 3
frutas = [ "Naranja", "Manzana", "Pera", "Pera"] 
partes = frutas[1]
print(partes)


longitud = len(frutas)
print(longitud)


listaStrings = [ 'Hola', 'Mundo', 'Python']
listaNumbers = [ 1, 2, 3, 4, 5]
listaBooleans = [ True, False, True]
listaMixta = ["Alfa", 1, True]
print(listaMixta)

tipo = type(listaBooleans)
print(tipo)

listaDesdeConstructor = list(("Beta", 2, True))
print(listaDesdeConstructor)

