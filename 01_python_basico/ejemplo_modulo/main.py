import edad as ed  # el ed es el difinitivo de la edad , forma de importar modulos

                    # fecha nacimiento     # fecha actual 
print(ed.calcula_edad("13/02/2000" , "18/02/2025"))

from edad import ce# importamos el modulo edad y la funcion calcula_edad, # con el os se puede colocar alias 


print(range.__doc__) # para ver la documentacion de un modulo



if __name__  == "__main__": # forma da esta seguro de que estamos llamando al fichero auxiliares, esto es un modulo
   print(ce("13/02/2000" , "18/02/2025"))
   print(ce.__doc__)

# modulos -> los modulos son archivos de codigo que se pueden importar en otros archivos
# modulos -> son paquetes que ya vienen con python por ejemplo Imagen, math, os, sys, etc

