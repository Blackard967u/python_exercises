# La encapsulación se refiere a impedir el acceso a determinados métodos y atributos 
# de los objetos estableciendo así que puede utilizarse desde fuera de su clase

# Esto se consigue en otros lenguajes, como Java, con modificadores de acceso.

# En python no existen los modificadores de acceso, lo que se suele hacer 
# es que una variable o función  viene determinada por su nombre: si el 
# nombre comienza con dos guiones bajos se trata de una variable o funcion 
# privada, en caso contrario es pública.

class Ejemplo:
    def publico(self):
        print("Publico")
    
    def __privado(self):
        print("Privado")

ej = Ejemplo()

ej.publico()

#Esto manda error, esto se debe a que los nombres que comienzan con un doble 
# guion bajo se renombran para incluir el nombre de la clase
# Esta caracteristica es conocida como "name mangling".
#Realmente el método no es privado

#ej.__privado()

#ej._Ejemplo_privado()

# En ocasiones puede que se quiera permitir el acceso a algún atributo 
# del objeto de manera controlada. Para esto se utilizan metodos cuya
# unica funcion sea esta, estos métodos son conocidos como "getters" y "setters"

class Fecha():
    def __init__(self):
        self.__dia = 1
    
    def getDia(self):
        return self.__dia
    
    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
            return self.__dia
        else:
            print("Error")

mi_fecha = Fecha()

dia = mi_fecha.getDia()

print(dia)
dia = mi_fecha.setDia(3)

print(dia)

print("-----------------------------------")

class Fecha(object):
    def __init__(self):
        self.__dia = 1
    def getDia(self):
        return self.__dia

    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
            return self.__dia
        else:
            print("Error")

    dia = property(getDia, setDia)


mi_fecha = Fecha()

dia = mi_fecha.getDia()

print(dia)
dia = mi_fecha.setDia(3)

print(dia)