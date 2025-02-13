# # DICCIONARIOS  -- > el acceso al dato se produce mendiante un  indentificador
# # llamado "clave". Asi: "Clave" : "Valor" 

# # la clave puede ser un string, un numero, una tupla.. 

#  # {} <- llaves 

# dic_1 = {} # diccionario vacio
# lista_1 = [] # lista vacia 

# if not lista_1:
#     print("La lista esta vacia") 

# dic_1 = { "Nombre": "Maria", "apellido": "Callas " , "edad": 53}
# print(dic_1["Nombre"]) 



# clave = "direccion" 

# print(dic_1.get(clave , f" la clave {clave} no existe en el diccionario ")) # get() devuelve None si no existe la clave 

# # con propiedad nos devuelve el valor de la clave

# for propiedad in dic_1:  # iteracion directa
#     print(propiedad)

# for propiedad in dic_1.keys:  # iteracion espeficica de claves
#     print(propiedad)

# for propiedad in dic_1.values:  # iteracion espeficica de valores
#     print(propiedad)

# for clave, valor in dic_1.items :  # iteracion espeficica de claves y valores
#     print(f"{clave} : {valor}") 

# # añadir un par de clave-valor 

# dic_1["Pais"] = "Grecia" #  se le pasa el valor y luego el nombre de la clave
# print(dic_1)

# # valores de actualizacion 

# dic_actualizacion = {"ciudad": "Paris" , "edad" : 50} 
# dic_1.update(dic_actualizacion) # actualizar diccionario 

# ----------------------------------- # 

# EJERCICIO 

# # Tenemos un sitio que registra los accesos de los usuarios, 

# # asi que necesitamos un menu con estas opciones 

# 1. añadiremos un usuario ( si no existe ya )
# 2. añadiremos una visita al usuario indicado ( si el usuario no existe mostrar el error)
# 3. mostraremos las visitas del usuario que se decida  ( si el usuario no existe mostrar el error)
# 4. mostraremos las visitas de todos lo usuarios ( si no hay usuarios todavia indicarlo )
# X. Salir 



"""
EJERCICIO DICCIONARIOS

Tenemos un sitio que registra los accesos de los usuarios.

Necesitamos un menú con estas opciones
1. Añadiremos un usuario 
        (si no existe ya)
2. Añadiremos una visita al usuario indicado 
        (si el usuario no existe mostrar el error)
3. Mostraremos las visitas del usuario que se decida
        (si el usuario no existe mostrar el error)
4. Mostraremos las visitas de todos los usuarios
        (si no hay usuarios todavía indicarlo)
X. Salir

Consideraremos que el nombre de cada usuario es único

"""

# import os
# os.system("cls")

# # Diccionario para almacenar usuarios y visitas
# users = {}

# while True: # creamos un while para que nos muestre el menu y las opciones 
#     menu = """
# 1. Añadir usuario nuevo
# 2. Añadir visita a un usuario
# 3. Mostrar visitas de un usuario
# 4. Mostrar visitas de todos los usuarios
# X. Salir
"""
#     print(menu)
#     opcion = input("Elige tu opción --> ").strip().lower()

#     match opcion: # hacemos un match para que se ejecute la opcion que elijamos

#         case "1": # el case 1 nos regista un nuevo usuario 
#             new_user = input("Nuevo usuario --> ").strip().title()

#             # Verificamos si el usuario ya existe
#             if new_user in users:
#                 print(f"El usuario '{new_user}' ya existe.") # imprimimos mensaje de error
#             else:
#                 users[new_user] = 0  # Se inicializa con 0 visitas
#                 print(f"Usuario '{new_user}' añadido correctamente.")  # añadimos un else con print para mostrar el usuario añadido 

#         case "2": # el case 2 nos añadir una visita de un usuario
#             if not users: # si user no esta registrado, nos muestra el print de abajo y no añade una visita
#                 print("No hay usuarios registrados. Añade un usuario primero.")
#             else: # hacemos un else para colocar el nombre del usuario y posterio añadir una visita 
#                 user_name = input("Nombre del usuario --> ").strip().title() # colocamos el nombre del usuario 
#                 if user_name in users: # si user esta registrado se le agrega una visita 
#                     users[user_name] += 1 # el +=1 nos agrega visitas el usuario 
#                     print(f"Visita añadida para '{user_name}'.") #  hacemos un print para las visitas del usuario 
#                 else:
#                     print(f"El usuario '{user_name}' no existe.") # y si no nos muestra que el usuario no esta registrado 

#         case "3": # hacemos un 3 case para mostrar las visitas del usuario 
#             if not users: # si use no esta registrado nos muesta el print de abajo 
#                 print("No hay usuarios registrados.")
#             else: 
#                 user_name = input("Nombre del usuario --> ").strip().title() # colocamos el nombre del usuario 
#                 if user_name in users: # al colocar el nomnre del usuario en la 
#                     # condicion de if se verifica si el usuario esta registrado
#                     print(f"'{user_name}' tiene {users[user_name]} visitas.") # si esta registrado nos muestra las visitas del usuario
#                 else:
#                     print(f"El usuario '{user_name}' no existe.") # si no esta registrado nos muestra que el usuario no existe

#         case "4": # hacemos un case 4 para mostrawr las visitas del usuario
#             if not users: # si user no esta registrado nos muestra el print de abajo 
#                 print("No hay usuarios registrados.")
#             else:
#                 print("\nVisitas por usuario:") # nos muestra las visitas del usuario 
#                 for user, visitas in users.items(): # 
#                     print(f"{user}: {visitas} visitas")

#         case "x":
#             print("Fin del programa")
#             break

#         case _:
#             print("Opción no reconocida. Vuélvelo a intentar.")

# print("\nUsuarios registrados:", users)


# Ejercicio 3 
"""


"""

Vamos a crear una app para vender entradas del cine.

Hay tres precios: 
- Entrada estándar: 9.00
- Mayores de 65 años (seniors) : 6.90
- Infantiles : 7.20

Se puede vender cualquier cantidad de entradas,
pero los menores siempre deber ir acompañados
de un adulto.

Al finalizar la compra mostraremos las entradas 
y el importe total. 

en cualquier momento hay que poder finalizar el proceso sin que se produzca la compra 

"""

# Precios de las entradas
PRECIOS = {
    "estandar": 9.00,
    "senior": 6.90,
    "infantil": 7.20
}

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Añadir entrada estándar")
    print("2. Añadir entrada senior (mayores de 65 años)")
    print("3. Añadir entrada infantil")
    print("4. Finalizar compra y mostrar total")
    print("X. Cancelar compra y salir")

# Bucle principal para ejecutar el menú
entradas_estandar = 0
entradas_senior = 0
entradas_infantil = 0

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ").strip().upper()
    
    if opcion == "1":
        entradas_estandar += 1
        print("Entrada estándar añadida.")
    elif opcion == "2":
        entradas_senior += 1
        print("Entrada senior añadida.")
    elif opcion == "3":
        if entradas_estandar > 0 or entradas_senior > 0:
            entradas_infantil += 1
            print("Entrada infantil añadida.")
        else:
            print("Error: Los menores deben ir acompañados de un adulto.")
    elif opcion == "4":
        total = (entradas_estandar * PRECIOS["estandar"] +
                 entradas_senior * PRECIOS["senior"] +
                 entradas_infantil * PRECIOS["infantil"])
        print("\nResumen de la compra:")
        print(f"Entradas estándar: {entradas_estandar}")
        print(f"Entradas senior: {entradas_senior}")
        print(f"Entradas infantiles: {entradas_infantil}")
        print(f"Importe total: {total:.2f} €")
        break
    elif opcion == "X":
        print("Compra cancelada. Saliendo...")
        break
    else:
        print("Opción no válida, vuelve a intentarlo.")