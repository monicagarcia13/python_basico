# Esto es un comentario de una linea de Python 

# Variables:
# Es un contenedor para almacenar valores de datos.
# Este contenedor va a tener un nombre.
# Es creada la primera vez que se le asigna un valor

# NOMBRES ADMITIDOS DE VARIABLES

# 1. Puede empezar con una letra o un guión bajo (underscore)
mivariable = "texto"
_mivariable = "otro texto"

# 2. No puede iniciar con un número
### 5variable = "texto"

# 3. Sólo pueden contener caracteres alfanuméricos y guiones bajos (A-z 0-9 _)
miVariable123_ = "texto"
_123miVariable_123 = "texto"

# 4. CaseSensitive (no solo al comienzo sino en general)

miVariable = "otro texto"
MiVariable = "otro texto"

# 5. No se puede utilizar palabras reservadas de Python (keywords)

asd123 = "informacion"

#####################

# Convenciones de escritura de variables

# Camel Case
camelCase = "Comienza con minúscula y cada palabra siguiente comenzará con mayúscula"

# Pascal Case
PascalCase = "Comienza con mayúscula y cada palabra siguiente comenzará con mayúscula"

# Snake Case
snake_case = "Se usan las palabras en minúscula y las palabras son separadas con guiones bajos"

#####################

# Multiasignación

x, y, z = 5, 7, 9
a = b = c = "Sergie Code"

# Desde colecciones
frutas = ["naranja", "banana", "mandarina"]
m, n, o = frutas

# Uso de print y salidas:

txt = "Curso"
txt2 = "de "
txt3 = "Python"

num1 = 2
num2 = 4
num3 = 6

# Variables globales vs Variables de Scope

variableGlobal = "Esta variable va a estar disponible para todo el programa"

def funcion():
    global variableDeScope
    variableDeScope = "Esta variable sólo estará disponible dentro del alcance de la función"
    variableGlobal = "Este valor es sólo para dentro de la función y luego recupera su valor"
    print(variableGlobal)
    print(variableDeScope)

funcion()

print(variableGlobal)
print(variableDeScope)

"""
CARACTERÍSTICAS BÁSICAS DE PYTHON
"""

# VARIABLES
# Una variable es un espacio en memoria para guardar datos
# por tanto, es un contenedor

# Para crear una variable...
# identificador = valor

# Hay reglas para llamar a los identificadores = nombre de la variable 
# No se puede hacer:
#   1variable (empezar por un número, después si lo puede llevar)
#   $variable (ni empezar ni contener símbolos especiales)
# De estos errores nos avisará VSC 

# No debemos hacer (no son exactamente errores):
#     Contener caracteres fuera del idioma inglás, como ñ, Ç, tildes, á, ö, etc
#     Empezar por guión bajo (reservado para determinadas situaciones)

# Qué debemos hacer:
#     Nombrar a nuestras variables con palabras descriptivas
#     Podemos usar más de una palabra separadas por un guión bajo (directiva PEP-8)
#     Intentar que las línes de código no sean muy largas

# las variables tiene tipo 

#--Numeros => enteros (int) , decimales (float), complejos
#--Texto => cadenas de caracteres (str)
#--Booleanos => True, False

# PYTHON ES DE TIPADO DINAMICO 

numero = 1 # entero 