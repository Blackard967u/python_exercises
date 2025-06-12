#lista 
l = [32, True, "una lista", [1, 2]]

#imprime la lista en el indice 2
print(l[2])

#imprime el elemento de una lista incluida dentro de otra lista
print(l[3][1])

#podemos modificar el valor de una lista
l = [42, False, "Otra lista"]
print(l[2])

#si se utiliza un número negativo como indice, se buscará el valor del final al inicio
print(l[-2])


#-----------slicing o particionado-----------------------
ln = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#nos devuelve una porción de lista entre los indices definidos
print(ln[4:11])


#nos devuelve una porcion de lista, pero el tercer valor indica cada cuantos saltos añadir un valor
#a la lista
print(ln[4:11:3])

#los numeros negativos también se utilizan en el slicing
print(ln[4:-1:2])

#No es necesario agregar el principio y el final del slicing
#se usaran por defecto las posiciones de inicio y fin de la lista
print(ln[:10])

print(ln[10:])

print(ln[:])

print(ln[::2])


#podemos modificar una lista  usando slicing

ln[0:2] = [False, "Attr añadido", "otro atributo extra"]

print(ln[:])

# ---------------------------------Métodos comunes------------------------------------------------
print("------------------------------------------------------")
#lista 
l = [32, True, "una lista", [1, 2], True]


l.append([23, 24])

print(l)

# append() permite añadir un objeto al final de la lista

print("------------------------------------------------------")


l.extend(["c", "d"])

print(l)

# extend() añade varios elementos al ginal de la lista

print("------------------------------------------------------")

l.insert(1, 2)

print(l)

# insert() añade un elemento en una posicion específica

print("------------------------------------------------------")

l.remove(True)

print(l)

# remove() elimina la primera aparición de un documento

print("------------------------------------------------------")

ultimo = l.pop()

print(ultimo)
print(l)

# pop() elimina y devuelve el último elemento

print("------------------------------------------------------")

index = l.index(True)

print(index)

# index() devuelve el indice de la primera aparición del elemento

print("------------------------------------------------------")

li = l.count(True)

print(li)

# count() permite contar la cantidad de veces que aparece el valor en la lista

print("------------------------------------------------------")

l.reverse()

print(l)

# reverse() permite revertir el orden de la lista

print("------------------------------------------------------")



















l.clear()

print(l)

# clear() elimina todos los elementos de la lista

print("------------------------------------------------------")



















