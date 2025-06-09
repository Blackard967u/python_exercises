# El polimorfismo se refiere a la habilidad de los objetos de distintas clases
# responder al mismo mensaje. Esto se consigue a través de la herencia:
# un objeto de la clase derivada es al mismo tiempo un objeto de la clase padre
# de forma que allí donde se requiere un objeto de la clase padre también
# se puede utilizar uno de la clase hija

class Animal:
    def hacer_sonido(self):
        print("El animal hace un sonido")

class Gato(Animal):
    def hacer_sonido(self):
        print("El gato maúlla")

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro ladra")

animal = Animal()

animal.hacer_sonido()

print("--------------------------------")

gato = Gato()

gato.hacer_sonido()

print("--------------------------------")

perro = Perro()

perro.hacer_sonido()


# En ocasiones también se utiliza el término polimorfismo para referirse a la sobrecarga
# de métodos, término que se define como la capacidad del lenguaje de determinar qué
# método ejecutar de entre varios métodos con igual nombre según el tipo o número de
# los parámetros que se le pasa.

# En Python no existe sobrecarga de métodos (el último
# método sobreescribiría la implementación de los anteriores).