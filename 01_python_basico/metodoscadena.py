# Métodos de cadena
# Existen muchos métodos de cadenas que nos permiten formatear cadenas. Vea algunos de los métodos de cadenas en el siguiente ejemplo:

# capitalize(): Convierte el primer carácter de la cadena en letra mayúscula

challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

# count(): devuelve las ocurrencias de la subcadena en la cadena, count(subcadena, inicio=.., fin=..).
#  El inicio es un índice inicial para el conteo y el fin es el último índice para contar.

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`

# endswith(): Comprueba si una cadena termina con una terminación especificada

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# expandtabs(): reemplaza el carácter de tabulación con espacios, el tamaño de tabulación predeterminado es 8. Toma el argumento de tamaño de tabulación

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# find(): Devuelve el índice de la primera aparición de una subcadena, si no se encuentra, devuelve -1

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# rfind(): Devuelve el índice de la última aparición de una subcadena, si no se encuentra, devuelve -1

challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17

# format(): formatea la cadena para obtener una salida más agradable.
# Para obtener más información sobre el formato de cadenas, consulte este enlace.

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314


# index(): 
# devuelve el índice más bajo de una subcadena; 
# los argumentos adicionales indican el índice inicial y final (valor predeterminado: 0 y longitud de la cadena: 1).
#  Si no se encuentra la subcadena, se genera un valueError.

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error


# rindex(): Devuelve el índice más alto de una subcadena, los argumentos adicionales indican el índice inicial y final (valor predeterminado 0 y longitud de la cadena - 1)

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on', 8)) # 19



# isalnum(): Comprueba caracteres alfanuméricos

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False


# isalpha(): Comprueba si todos los elementos de la cadena son caracteres alfabéticos (az y A-Z)

challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False


# isdecimal(): Comprueba si todos los caracteres de una cadena son decimales (0-9)

challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed

# isdigit(): Comprueba si todos los caracteres de una cadena son números (0-9 y algunos otros caracteres Unicode para números)

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True


# isnumeric(): Comprueba si todos los caracteres de una cadena son números o están relacionados con números (al igual que isdigit(), solo que acepta más símbolos, como ½)

num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False


# isidentifier(): comprueba si hay un identificador válido: comprueba si una cadena es un nombre de variable válido

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

# islower(): Comprueba si todos los caracteres del alfabeto en la cadena están en minúsculas

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): Comprueba si todos los caracteres del alfabeto en la cadena están en mayúsculas

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True

# join(): Devuelve una cadena concatenada
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

# strip(): elimina todos los caracteres dados comenzando desde el principio y el final de la cadena

challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'

# replace(): reemplaza la subcadena con una cadena dada

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split(): divide la cadena, utilizando la cadena dada o el espacio como separador

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

# title(): Devuelve una cadena con título en mayúsculas y minúsculas

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

# swapcase(): Convierte todos los caracteres en mayúsculas en minúsculas y todos los caracteres en minúsculas en mayúsculas

challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Comprueba si la cadena comienza con la cadena especificada


challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False 
