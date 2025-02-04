# print("Hola, soy un programa de prueba")

# a = int(input("Ingresa el primer numero:"))
# b = int(input("Ingresa el segundo numero:"))

# print("La suma es", a + b)


# num = int(input("Ingresa un numero:"))

# if num % 2 == 0:
#     print("El numero es par")

# else:
#     print("El numero es impar")


# texto = input("Ingresa una palabra ") 
# print("Palabara invertida", texto[::-1])


# n = int(input("Cantidad de términos: "))
# a, b = 0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


# n = int(input("Cantidad de números: "))
# print([i ** 2 for i in range(1, n + 1)])

# import random
# import string

# longitud = int(input("Longitud de la contraseña: "))
# caracteres = string.ascii_letters + string.digits + string.punctuation
# contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
# print("Contraseña generada:", contraseña)

import random
print("Número del dado:", random.randint(1, 7))
