"""
MATCH = switch de JS o JAVA
"""

mes = "Febrero"

match mes:
    case "Enero":
        print("Iré a NY")
    case "Febrero":
        print("Iré a Paris")
    case "Marzo" | "Abril" | "Mayo":
        print("Iré a Londres")
    case _ :
        print("No sé a dónde iré")

'''
Ejercicio
Preguntar al usuario qué día de la semana es (lunes, martes, ...)
Si dice lunes diremos : "Toca sistemas"
Si dice "martes, miércoles, jueves o viernes", diremos : "Toca Python"
Si dice sábado o domingo diremos : "Es fin de semana!!!"
Si dice otra cosa diremos: "Creo que estás confundido/a"

'''

