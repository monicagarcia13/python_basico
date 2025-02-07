# Vamos a pedir un número entero al usuario
# Con él imprimiremos la tabla de multiplicar del 1 al 10

num = int(input("Escribe un numero ->")) # pedimos un numero entero al usuario
for i in range(1, 11): # generamos una secuencia desde 1 hasta 10
    print(f"{num} x {i} = {num * i}") 
    # multiplicamos num por i y lo imprimimos 


