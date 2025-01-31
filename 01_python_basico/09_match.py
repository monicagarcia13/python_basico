# # MATCH = switch de JS  o JAVA

# mes = "Octubre"

# match mes: 
#     case "Enero":
#         print("Ire a NY")
#     case "Febrero":
#         print("Ire a paris")
#     case "Marzo" | "Abril" | "Mayo":
#         print("Ire a Londres")
#     case _ : 
#         print("No se a donde ire")

#     # la _ equivale a default 

# try:
#     #pedimos los numeros
#     num_1 = float(input("Escribe el primer número -> "))
#     num_2 = float(input("Escribe el segundo número -> "))
#     print( '''
# Opciones:
#           suma
#           resta
#           multplicacion
#           division
#           división_entera
#           modulo
# ''')
#     operacion = input("¿Qué operación quieres realizar?")
#     match operacion:
#         case "suma":
#             print(f"{num_1} + {num_2} = {num_1 + num_2}")
#         case "resta":
#             print(f"{num_1} - {num_2} = {num_1 - num_2}")
#         case "multiplicacion":
#             print(f"{num_1} * {num_2} = {num_1 * num_2}")
#         case "division":
#             print(f"{num_1} / {num_2} = {num_1 / num_2}")
#         case "división_entera":
#             print(f"{num_1} // {num_2} = {num_1 // num_2}")
#         case "exponente":
#             print(f"{num_1} ** {num_2} = {num_1 ** num_2}")
#         case "modulo":
#             print(f"{num_1} % {num_2} = {num_1 % num_2}")
#         case _:
#             print("Opcion no valida")
# except ValueError:
#     print("Error: Debes introducir un numero valido...")

#Ejercicio

#Vamos a preguntar que dia de la semana es 
#Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo
# si dice lunes diremos : "Toca sistemas"
# si dice "Martes, miercoles, jueves y viernes diremos: "Toca Python" 
#si dice sabado o domingo diremos: "Es fin de semana" 
#si dice otra cosa diremos: "Creo que estas confundido"

dia = input("¿Que dia de la semana es ->").lower()

match dia:
    case "lunes":
        print("Toca sistemas")
    case "martes" | "miercoles" | "jueves" | "viernes":
        print("Toca Python")
    case "sabado" | "domingo" | "sabadó":
        print("Es fin de semana!!!")
    case _:
        print("Creo que estas confundido/a")


