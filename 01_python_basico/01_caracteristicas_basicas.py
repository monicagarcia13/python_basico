"""
CARACTERÍSTICAS BÁSICAS DE PYTHON
"""

# =============================================================
'''
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

No debemos hacer (no son exactamente errores):
    Contener caracteres fuera del idioma inglás, como ñ, Ç, tildes, á, ö, etc
    Empezar por guión bajo (reservado para determinadas situaciones)
    Utilizar palbras reservadas del sistema (True, False, etc)

Qué debemos hacer:
    Nombrar a nuestras variables con palabras descriptivas
    Podemos usar más de una palabra separadas por un guión bajo (directiva PEP-8)
    Intentar que las línes de código no sean muy largas

Las variables tienen tipo
    -- números -> enteros (int), decimales (float), complejos
    -- texto -> strings
    -- booleanos -> True / False
    --

En Python, por defecto NO existen las constantes
PI = 3.1416
PI = 2.45

PYTHON ES DE TIPADO DINÁMICO

numero = 1 # entero
numero = "uno" # string

PYTHON ES DE TIPADO FUERTE

suma = numero + 2 # Error -> no se pueden sumar números y texto
concatenacion = numero + str(2)
suma_numerica = int("1") + 2

'''

