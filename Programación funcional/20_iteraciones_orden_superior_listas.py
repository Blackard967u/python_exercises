from functools import reduce

# Con las funciones de orden superior podemos pasarlas como argumentos de la funciones 
# map, filter y reduce. Funciones que permiten sustiuir los bucles típicos de los lenguajes 
# imperativos mediante construcciones equivalentes.

# Función map()

#La función map() aplica una función a cada elemento de una secuencia y devueve una lista con
# el resultado para aplicar la función a cada elemento. Si se pasan como parámetros n secuencias,
# la función tendrá que aceptar n argumentos. Si alguna de las secuencias es más pequeña que las 
# demás, el valor que le llega a la función function para posiciones mayores que el tamaño de 
# dicha secuencia será "None"

# map(function, secuence[,secuence,...])

def cuadrado(n):
    return n**2

l = [1,2,3]

l2 = map(cuadrado, l)

print(list(l2))

print("--------------------------")

# Funcion filter()

# Esta funcion verifica que los elementos de una secuencia cumplan una determinada condición
# devolviendo los elementos que cumplen la condición  

def es_par(n):
    return (n % 2 == 0)

l = [1,2,3,4,5,6,7]

l2 = filter(es_par, l)

print(list(l2))

print("--------------------------")

# Funcion reduce()

# Esta funcion aplica una función a pares de elementos de una secuencia hasta dejarla
# en un solo valor.

def sumar(x,y):
    return x +y
l = [1,2,3,4,5,6]

l2 = reduce(sumar,l)

print(l2)