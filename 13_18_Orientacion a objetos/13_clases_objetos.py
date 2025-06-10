# Un objeto es una entidad que agrupa un estado y una funcionalidad relacionadas

#El estado del objeto se define a través de variables llamadas atributos,
# y la funcionalidad se modela a través de funciones las cuales se conocen
# como métodos del objeto

#-------------Ejemplo de objeto ---------------

#Un coche podría ser un objeto, donde coche tiene como atributos 
# la marca, el número de puertas, el tipo de carburante
# y tiene como métodos arrancar y parar


# Una clase, por otro lado, es la plantilla genérica de la cual se 
# se instanciarán objetos, la plantilla es la que define qué atributos 
# y métodos tendrán los objetos de esa clase

# En python las clases se definen usando la palabra clave "class" seguida
# del nombre de la clase y dos puntos ":", y a continuación el identado.

class Coche:
    """Abstracción de los objetos coche"""
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print("tenemos", gasolina, "litros")

    def arrancar(self):
        if self.gasolina>0:
            self.gasolina-=1
            print("Quedan", self.gasolina, "litros")
        else:
            print("No arranca")
    
    def conducir(self):
        if(self.gasolina>0):
            self.gasolina -= 1
            print("Quedan", self.gasolina, "litros")
        else:
            print("No se mueve")

# El método "__init__" se ejecuta justo después de crear un nuevo objeto
# a partir de la clase, este proceso se conoce como "instanciación".
# El método __init__ sirve para realizar cualquier proceso de inicialización
# que  sea necesario

# El primer parámetro y del resto de modulos es siempre "self".
# Esto es necesario para referirse al objeto actual.
# Es necesario para poder acceder a los atributos y métodos del objeto diferenciado

#para crear un objeto se escribe el nombre de la clase seguidode cualquier parámetro
# que sea necesario

mi_coche = Coche(3)
print("------------------------------")
# Ahora que el objeto se ha creado, se puede acceder a sus atributos

mi_coche.arrancar()
print("------------------------------")

mi_coche.conducir()