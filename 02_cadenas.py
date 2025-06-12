#cadena simple
cadena = "cadena cadena2 "

print(cadena)
#cadena triple, para mostrar en varias  lineas
triple = """primera linea, 
otra linea, 
y otra linea"""

print(triple)
#suma de cadenas
sum_cadena = "Hola "+"Mundo" 

print(sum_cadena)
#multiplicacion de cadena, repite  la cadena las veces solicitadas
mult_cadena = "Hola mundo"*3

print(mult_cadena)

print("-----------------------------------------------")
##print(dir(str))


# upper() convierte la cadena a mayúsculas
a = cadena.upper()

print(a)

print("-----------------------------------------------")

# lower() convierte la cadena a minúsculas
a = cadena.lower()

print(a)

print("-----------------------------------------------")

# capitalize() capitaliza la primera letra de la cadena 
a = cadena.capitalize()

print(a)

print("-----------------------------------------------")

# title() capitaliza cada palabra
a = cadena.title()

print(a)

print("-----------------------------------------------")

# strip() elimina los espacios al inicio y al final
a = cadena.strip()

print(a)

print("-----------------------------------------------")

# lstrip() elimina los espacios a la izquierda
a = cadena.lstrip()

print(a)

print("-----------------------------------------------")

# rstrip() elimina los espacios a la derecha
a = cadena.rstrip()

print(a)

print("-----------------------------------------------")

# replace() permite reemplazar un fragmento de cadena
a = cadena.replace("cadena2", "cadena3")

print(a)

print("-----------------------------------------------")

# find() encuentra en el indice de la primera ocurrencia
a = cadena.find("n")

print(a)

print("-----------------------------------------------")

# startswith() verifica si la cadena inicia con una subcadena
a = cadena.startswith("cad")

print(a)

print("-----------------------------------------------")

# endswith() verifica si la cadena termina con una subcadena
a = cadena.endswith("en")

print(a)

print("-----------------------------------------------")


# isalpha() verifica si la cadena solo contiene letras
a = cadena.isalpha()

print(a)

print("-----------------------------------------------")

# isdigit() verifica si la cadena solo contiene dígitos
a = cadena.isdigit()

print(a)

print("-----------------------------------------------")

# isalpha() verifica si la cadena contiene numeros y letras sin espacios
a = cadena.isalnum()

print(a)

print("-----------------------------------------------")
