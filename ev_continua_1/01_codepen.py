# El usuario introduce un número entero, como máximo 100
# ese número es el límite
# Desde 0 hasta el número introducido (los dos incluidos), vamos a listar todos los números
# Pero...
# -- Si el número es multiplo de 3, escribiremos 3 - FIZZ
# -- Si el número es multiplo de 5, escribiremos 5 - BUZZ
# -- Si el número es multiplo de 3 y de 5, escribiremos 3 - FIZZ-BUZZ
# -- En los demás casos sólo el número
# -- Si el usuario escribe más de 100 o menos de 0, diremos "El número es incorrecto"

num = int(input("Escribe un numero (maximo 100):"))  # input solicita un numero entero 
# int convierte el texto introducido al número entero

if num < 0 or num > 100: # ponemos la condicion de if si el número introducido es mayor o menor que 100
    print("El numero es incorrecto")
else: 
    for i in range(0, num + 1): # genera una secuencia desde 0 hasta num 
        texto = f"{i} - " # creamos una variable texto para guardar el resultado
        if i % 3 == 0: # verifica si i  es divisible por 3 
            texto += "FIZZ" # si es verdadero concatenamos FIZZ
        if i % 5 == 0:  # verifica si i es divisible por 5
            texto += "BUZZ" # si es verdadero concatenamos BUZZ
        print(texto if texto != f"{i} - " else i) 
        # Si texto cambió (es decir, i es múltiplo de 3 o 5), imprimimos texto.
        #Si texto NO cambió (es decir, i NO es múltiplo de 3 ni 5), imprimimos solo i.