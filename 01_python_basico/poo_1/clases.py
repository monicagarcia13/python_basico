# para crear clases seria la palabra clave class

class Persona():
    """
    Propiedades de una persona
    """
    # caracteristica de una persona son atributos 
    # los metodos propios de python viene asi __init__

    # Metodo de instacia 
    def __init__(self, nombre, apellido, funcion): # estos son parametros , asigno caracteristicas y luego se llama al constructor
        self.nombre = nombre
        self.apellido = apellido
        self.funcion = funcion
    
    def __str__(self):
        return  f"Nombre:{self.nombre}, apellido:{self.apellido}, funcion:{self.funcion}"

    
        

# un objeto es la instancia de una clase 

persona_1 = Persona("Monica", "Garcia", "alumna")
print(type(persona_1))

# asi se pueede cambiar el nombre de la persona
persona_1.nombre = "Monica"
print(persona_1) 

#Abstraccion -> 
# Encapsulamiento -> 
# polimorfismo -> Puedes tener algo que este en diferentes tipos de objetos 
#sobrecarga -> yo tengo un objeto y quiero que pueda ser de diferentes tipos de objetos (en python no)
# herencia -> 


