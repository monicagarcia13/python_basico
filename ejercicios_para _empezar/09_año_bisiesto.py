'''
EJERCICIO 9: AÑO BISIESTO
Haz un programa que pida al usuario un año y diga si es bisiesto o no
Averigua cual es el criterio
'''

año = int(input("Introduce un año => "))

if año % 400 == 0:
    print(f"{año} es bisiesto")
elif año % 100 == 0:
    print(f"{año} no es bisiesto")
elif año % 4 == 0:
    print(f"{año} es bisiesto")
else:
    print(f" el año NO es bisiesto") 


