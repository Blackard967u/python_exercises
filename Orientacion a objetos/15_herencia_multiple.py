# En Python a diferencia de otros lenguajes existe algo que se conoce como 
# Herencia Multiple, tal como su nombre lo dice, esto le permite a una clase heredar
# de multiples clases (superclases) a la vez.

class Terrestre:
    def desplazar(self):
        print("El animal camina")

class Acuatico:
    def desplazar(self):
        print("El animal nada")

    
# Es importante tener en cuenta, que si ambas superclases tienen un método que se nombre
# igual, la subclase tomará el método de la superclase que se encuentre más a la 
# izquierda
class Cocodrilo(Acuatico, Terrestre):
    pass

c = Cocodrilo()

c.desplazar()

print("---------------------------")

class Cocodrilo(Terrestre, Acuatico):
    pass

c2 = Cocodrilo()

c2.desplazar()