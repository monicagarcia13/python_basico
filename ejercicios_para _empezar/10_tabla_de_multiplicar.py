'''
EJERCICIO 10: TABLA DE MULTIPLICAR
Haz un programa que pida al usuario un número 
y muestre la tabla de multiplicar de ese número
desde 1 hasta 10, ambos incluidos
'''

num = int(input("Introduce un numero => "))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")

    

def tabla_multiplicar(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

numero = int(input("Introduce un número => "))
tabla_multiplicar(numero)
