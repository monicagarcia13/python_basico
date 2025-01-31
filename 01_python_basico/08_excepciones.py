# EXCEPCIONES 

# Son errores que se produceb  durante la ejecucion del programa y lo interumpen 

import os

os.system("cls")

# try / except
# si hay try debe haber un except 

try: 
   #intentamos ejecutar el codigo
   num = float(input("Escribe un numero..."))
   #print( 1/ 0)
   #print("Despues  de la division por cero")
except ValueError:
   print("Has de introducir un numero")

except: 
   #si se produce una excepcion, ejecutamos este otro codido 
   print("No se puede dividir por cero")

print("El programa continua...")



try: 
   #intentamos ejecutar el codigo
   num = float(input("Escribe un numero..."))
   #print( 1/ 0)
   #print("Despues  de la division por cero")
except ValueError: #Error de conversion de tipos
   print("Has de introducir un numero")

except ZeroDivisionError: #Error de división por cero
   #si se produce una excepcion, ejecutamos este otro codido 
   print("No se puede dividir por cero")

except:
   print("Ha ocurrido un error") #Error generico

print("El programa continua...")



