#funciona igual que las listas, pero en lugar de
#corchetes se utilizan parentesis
t = (1, 2, True, "Hola mundo")

print(t)

#imprime la clase de tipo que es "t", la cual es una tupla
print(type(t))

#es necesario agregar al menos una coma para que sea considerada una tupla
#sin coma
t=(1)
print(type(t))

#con coma
t = (1,)
print(type(t))

#utilizamos [] para referirnos a un elemento de una tupla

t = ("one", "two", "three", "four", "five", "six")
print(t[2])

##Las tuplas y las listas forman parte de un tipo de objetos llamados
#  SECUENCIAS, así que también podemos hacer cosas 
#como el slicing

print(t[2:4])

##Las tuplas no poseen mecanismos de modificación

