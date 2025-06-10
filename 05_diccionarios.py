## Diccionarios, también llamadas "Matrices Asociativas"

#el primer valor es una clave, el segundo valor es el valor asociado a la clave
music_d = { 
    "Avicci": "Wake Me Up", 
    "The Beatles":"Let It Be",
    "Freddie Mercury": "Bohemian Rhapsody" }

#para acceder a un valor usamos [] y la clave
print(music_d["Avicci"])

#podemos reasignar valores

music_d["Avicci"] = "The Nights"
print(music_d["Avicci"])

# En los diccionarios NO podemos utilizar slicing, 
#pero podemos utilizar mappings











#------------------------------------Métodos útiles de los diccionarios---------------------------------------

a = music_d.get('Martin Garrix', "No especificado")

print(a)

# El primer parametro es la clave a buscar dentro del diccionario, el segundo parámetro
# es el valor que devolverá si no se encuentra esa clave, es decir el valor por defecto.

print("--------------------------------------------------")

a = "Avicci" in music_d

print(a)

# Comprueba si el diccionario tiene la clave específicada y devuelve un valor booleano

print("--------------------------------------------------")


a = music_d.items()

print(a)

#  Devuelve una lista tuplas con pares clave-valor

print("--------------------------------------------------")

a = music_d.keys()

print(a)

# Devuelve una lista de las claves del diccionario

print("--------------------------------------------------")

a = music_d.values()

print(a)

# Devuelve una lista de los valores del diccionario

print("--------------------------------------------------")


a = music_d.pop('Avicci', "No especificado")

print(a)
print(music_d)

# Elimina el valor del diccionario y devuelve el valor de la clave


