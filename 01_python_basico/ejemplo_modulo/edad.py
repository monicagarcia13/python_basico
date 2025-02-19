"""
Devolver la edad a apartir de dos fechas

Params
fecha_nacimiento: str -> "dd/mm/yyyy" 
fecha_actual : str -> "dd/mm/yyyy"

return 
edad: int 

Codigos de error: 
-1 : dia o mes incorrecto
-2 la fecha de nacimiento debe de ser igual o menor que la actual 

"""

def calcula_edad(fecha_nacimiento: str, fecha_actual: str) -> int:
    # Convertir 
    fecha_actual = fecha_actual.split("/")
    dia_actual= int(fecha_actual[0])
    mes_actual = int(fecha_actual[1])
    anyo_actual = int(fecha_actual[2])
   
    fecha_nacimiento = fecha_nacimiento.split("/")
    dia_nacimiento = int(fecha_nacimiento[0])
    mes_nacimiento = int(fecha_nacimiento[1])
    anyo_nacimiento = int(fecha_nacimiento[2])

    if (not 1 <= mes_actual <= 12) \
        or (not 1 <= mes_nacimiento <= 12) \
            or (not 1 <= dia_actual <= 31) \
                or (not 1 <= dia_nacimiento <= 31):
                return -1

    dif_anyos = anyo_actual - anyo_nacimiento
    dif_meses = mes_actual - mes_nacimiento
    dif_dias = dia_actual - dia_nacimiento
    if (dif_anyos < 0) \
        or (dif_anyos == 0 and dif_meses < 0) \
            or (dif_anyos == 0 and dif_meses == 0 and dif_dias < 0):
                return -2
    
    # Calcular edad
    if (mes_nacimiento > mes_actual) :
            return dif_anyos - 1
    elif (mes_actual == mes_nacimiento and dia_nacimiento > dia_actual):
            return dif_anyos - 1
    else:
            return dif_anyos
   
edat = calcula_edad("13/02/2000" , "18/02/2025")
print("Tienes {edad} años".format(edad=edat))
    