"""
EJERCICIO 2 : ÁREA DE UN TRIÁNGULO
Haz un programa que pida al usuario dos números, 
indicando que son la base y la altura de un triángulo
La respuesta del programa será:
"El área de un triángulo de base X y altura Y es Z" (los valores que sean)
"""
base_triangulo = int(input("Introduce la base de un triángulo =>"))
altura_triangulo = int(input("Introduce la altura de un triangulo =>"))
total_area = (base_triangulo * altura_triangulo) / 2
print(F"el area de un triangulo de base {base_triangulo} y altura {altura_triangulo} es {total_area}")