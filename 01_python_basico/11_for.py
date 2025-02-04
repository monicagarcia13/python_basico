# BUCLE FOR 
import os 
os.system("cls")

# nombres = [ "Pol", "Pau", "Luis" , "Juan", "Pablo"]
           

# # para cada nombre en nombres ... 
# for nombre in nombres:  # se ejecutara una vez por cada nombre en nombres
#     if nombre.startswith("P"): # si comienza con "P" 
#         print(nombre)  # se imprimira el nombre


#  # Si el nombre comienza con "p" o "P"
# nombres = [ "Pol", "Pau", "Luis" , "Juan", "Pablo"]

# check = "p"

# for nombre in nombres: # se ejecutara una vez por cada nombre en nombres
#     if nombre.lower().startswith("p"): # es un metodo para palabras #si comienza con "p" o "P"
#         print(nombre) 


# for nombre in nombres:
#     if nombre[0].lower() == check.lower(): 
#         print(nombre.capitalize()) 

# ejercicio 2
#mostrar los numeros de esta lista que empiezan por dos , 

# edades = [ 25, 30, 35, 40, 45, 28, 28, 76, 89, 234 ]  #lista de edades

# #recorre la lista de edades 

# for edad in edades: 
#     if  str(edad)[0] == "2":
#         (print(edad))



# # Lista de edades
# edades = [25, 30, 35, 40, 45, 28, 28, 76, 89, 234]

# check = "2" 
# suma = 0
# elementos = 0
# promedio = 0

# for edad in edades:
#     if str(edad).startswith(str(check)):
#         print(edad, end =" " ) 

#         suma += edad
#         elementos += 1
#         promedio += edad

# print(f"\nLa suma de los elementos es: {suma}")
# print(f"\nHAY {elementos} elementos")
# print(f"\nEl promedio de lista es {promedio/len(edades)}")




#Ejercicio 3 

#Mostrar el resultado asi: 

#la suma de los elementos es X
#HAY x elementos
# el promedio de la lista es X 



# # Lista de edades
# edades = [25, 30, 35, 40, 45, 28, 28, 76, 89, 234] 

# # Inicializar variables
# suma = 0
# elementos = len(edades)  # Número total de elementos

# # Recorrer la lista de edades y sumar todas las edades
# for edad in edades:
#     suma += edad

# # Calcular el promedio
# promedio = suma / elementos

# # Imprimir los resultados
# print(f"La suma de todas las edades es: {suma}")
# print(f"Hay {elementos} elementos")
# print(f"El promedio de las edades es: {promedio}")



#mostrar si un nombre esta en la lista
 #Luis esta en la lista
 #Alba no esta en la lista

# nombres = ["Pol", "Pau", "Luis", "Juan", "Pablo", "paco"]

# nombres_a_buscar= ["Luis", "Alba"]

# for nombre in nombres_a_buscar:
#     if nombre in nombres:
#         print(f"{nombre} está en la lista")
#     else:
#         print(f"{nombre} no está en la lista")


nombres = ["Pol", "Pau", "Luis", "Juan", "Pablo", "paco"]
nombres_a_buscar = "Luis" # Alba
for nombre in nombres:
    print(nombre)
    if nombre.lower() == nombres_a_buscar.lower():
        print(f"{nombre} esta en la lista")
        break
else:
        print(f"{nombre} no esta en la lista")
     
#Quiero saber que nombre de la lista contiene la letra "o" 




nombres_con_o= []

for nombre in nombres: 
    indice = nombres.index(nombre)
    if "o" in nombre.lower():
        print(f"{indice + 1}. {nombre}")
        nombres_con_o.append(nombre)

print(nombres_con_o)

# el for depende de una lista de valores, 

print(list(range(10))) # range es un tipo de datos que print no sabe entender 

for num in range(10): # un bucle es un bloque de codigo que se ejecuta una vez por cada valor de una lista
    print(num)





    

 









        




