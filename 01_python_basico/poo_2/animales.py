class Animal():
    def __init(self, especie):

        self.especie = especie

    def __str__(self):
        return f"Mi especie es {self.especie}"
    
class Perro(Animal): 
    def sonido(self):
        print("Guauuuu")


milo = Perro("Perro")
milo.sonido()
print("milo")


class Gato(Animal):
    def sonido(self):
        print("Miauuu")


mishi = Gato("Siames")




print(Perro.__bases__) # devuelve una lista con las clases base de la clase
print(Animal.__subclasses__()) # devuelve una lista con las subclases de la clase