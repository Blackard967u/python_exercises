# En el lenguaje orientado a objetos cuando hacemos que una 
# clase (subclase) herede todos los atributos y métodos de 
# otra clase (superclase) se llama Herencia

# Al acto de heredar de otra clase también se le conoce a menudo como
# "extender de una clase"

# para indicar que una clase hereda de otra se coloca el nombre de la 
# clase de la que se hereda entre parentesis después del nombre de la clase

class Instrumento:
    def __init__(self, precio):
        self.precio = precio
    
    def tocar(self):
        print("Estamos tocando música")
    
    def romper(self):
        print("Eso lo tienes que pagar")
        print("Son", self.precio, "$$$")

class Bateria(Instrumento):
    pass

class Guitarra(Instrumento):
    pass


# Existe algo llamado "Sobre escritura de métodos" que se utiliza, por ejemplo
# cuando quisieramos especificar un nuevo parámetro a la hora de crear un objeto
# Para esto basta con escribir un numero método __Init__ dentro de la subclase
# que se ejecutaría en lugar del __Init__ de la super clase.

class Guitarra(Instrumento):
    def __init__(self, precio):
        self.precio = precio*2


# Puede que en otro caso se necesite sobreescribir un método de la clase padre, pero 
# que en ese método se quiera ejecutar en ese método no se necesite más que ejecutar 
# un par de instrucciones nuevas. Para ello se utiliza la sintáxis "Superclase.metodo(self, args)"
# para llamar al método de igual nombre de la clase padre

class Bateria(Instrumento):
    def __init__(self, precio):
        Instrumento().__init__(self, precio):
            self.precio = precio
