#RESUMEN SIMPLIFICADO DE LO ESENCIAL 


#SINTASIS BASICA
#python "indenta" los bloques de codigo 
#python diferencia de mayusculas a minusculas



#VARIABLES: Es un contenedor de un elemento, es un indentificador para publicar un  elemento guardado en la memoria 

#se declaran con el signo de igualdad = 

#se pueden declarar con el signo de igualdad =

# La variable siempre se declaran antes de se utilizadas 
#tambien deben ser iniciadas 

int = 1 
float = 1.0
string = "hola"
boolean = True #false 

# aunque sean vacios hay que indicar valores 

#string = ""
#int = 0
#lista = []


#OPERADORES 

# -- de tipo matematico : 
#suma (+), resta (-), multiplicacion (*), división (/), exponencial (**), división entera (//)
# el signo + permite concatenar stings 

saludo = "buenas" + "" + "tardes" 
repeticion = "hola" * 3

# -- de comparacion: 
# == (igual), != (diferente) , > (mayor), < (menor), >= (mayor o igual), etc

# -- de asignacion: 
# = (asignacion), += (suma y asignacion), -= (resta y asignacion), *= (multiplicacion y asignacion), /= (división y asignacion), etc
# -- siempre devuelve un valor booleano 
# -- tambien podemos comparar strings 

int = 5 
int = int + 5  # es lo mismo que int += 5

int += 5 # este es un poco mas optimo 

num_str ="5" 
num_int = int(num_str) #casting -> convierte un string a un entero 
num_5 = 5 
num_5_str = str(num_5) #casting -> convierte un entero a un string

#estructura de control 

#condicionales 
# if #condicion: -> ejecutara un codigo si la condicion es verdadera 
# if condicion / else ( para todo lo demas)
# if condicion / elif condicion 
# if condicion / elif condicion / else

#match -> variable 
#case valor : # si la variable tiene el valor indicado 
# se ejecuta el codigo siguiente 
# case _ : # equivale al "default" o un else 
