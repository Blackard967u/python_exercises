# Así como existe el método __init__. Existen otros métodos con significados 
# especiales, cuyos nombre siempre  comienzan y terminan con 2 guiones bajos

__init__(self, args)

# Método llamado después de crear el objeto para realizar tareas de inicialización.

__new__(cls, args)

# Este es un método exclusivo de las clases de nuevo estilo que se ejecuta antes del
# __init__ y que se encarga de construir y devolver el objeto en sí.

__del__(self)

# Método llamado cuanddo el objeto va a ser borrado. También llamado destructor, se 
# utiliza para tareas de limpieza

__str__(self)

#Método llamado para crear una cadena de texto que represente un objeto. Se utiliza 
# cuando se utiliza print para mostrar el objeto o cuando se usa la funcion
# str(obj) para crear una cadena a partir del objeto

__comp_(self, otro)

# Método llamado cuando se utilizan los operadores de comparación para comprobar si un 
# objeto es menos, mayor o igual que el objeto pasado como parámetro

__len__(self)

#Método llamado para comprobar la longitud del objeto.