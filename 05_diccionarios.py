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

