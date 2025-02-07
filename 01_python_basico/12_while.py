" WHILE = Mientras "


num = 5 
while num > 0:
    print(num) 
    num -= 1

else: 
    print("Has entrado en el else")


    
 # Decir cuántas monedas necesitas
moneda = 10

while True:
    
        prestamo = int(input("¿Cuántas monedas necesitas? "))
        
        if prestamo > moneda:
            print("No puedes prestar más, no tengo")
        elif prestamo < 0:
            print("No puedes prestar una cantidad negativa")
        else:
            print(f"Te he prestado {prestamo} monedas")
            break  # Salir del bucle si la cantidad es válida
   




# x = 1

# while x <= 10:
#     print(f"Hola a todos estoy dentro de un bucle y x vale {x}")
#     x += 1

#     if x == 5:
#         break # Esto hace que salga del bucle

#     if x == 15:
#         continue # saltea las líneas de acá en adelante

# else:
#     print(f"Ya no se cumplió la condición del bucle porque x es {x}")



# ## EJEMPLO PRACTICO

# while True:
#     print("No te olvides de suscribirte a mi canal @sergiecode")
#     respuesta = input("¿Desea salir? (s/n)").strip().lower()
#     if respuesta == 's':
#