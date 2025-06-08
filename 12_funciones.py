# Una función es un fragmento de código con un nombre asociado
# que realiza una serie de tareas.

# a los fragmentos de código que tienen un nombre asociado y 
# no devuelven valores se les llama "procedimientos" pero 
# en python no existen los procedimientos ya que si no se 
# especifica el tipo de valor de retorno la función
# devuelve "none(nada) que equivale a Null de Java"

# Declaración de función
def funcion(param1, param2):
    #podemos encontrarnos una cadena en la primera linea 
    #del cuerpo de la función, esto es lo que imprime el operador
    # "?" de python
    """Esta cadena se conoce como docstring"""
    print(param1)
    print(param2)

# Así se manda a llamar una función, se sigue el orden de los 
# parametros respectivamente
funcion("Hola Mundo", 2)

print("-------------------------------")

# Si queremos modificar el orden de los parametros, debemos indicar el nombre
# del parámetro al que asociar el valor a la hora
# de llamar a la función

funcion(param2 = 2, param1 = "Hola Mundo")

print("-------------------------------")

# El numero de valores que se pasan a la función, debe coincidir
# con el número de parametros que la función espera

# Los valores por defecto se pueden definir situando un signo de igual 
# después del nombre del parámetro

def funcion_men(texto, veces = 1):
    print(texto * veces)

funcion_men("Hola mundo")

print("-------------------------------")

# para definir con una cantidad de argumentos que varien
# se coloca un último parámetro, cuyo nombre debe
# precederse de un signo "*"

def varios_params(param1, param2, *otros):
    for val in otros:
        print(val)

varios_params(1,2)
varios_params(1,2,3)
varios_params(1,2,3,4)

# lo anterior funciona creando una tupa en la que se almacenan los valores de todos los parametros extra.

print("-------------------------------")

# También en lugar de "*" se puede utilizar "**", en cuyo caso en lugar
# de una tupla se utilizaría un diccionario

def varios_dicc(param1, param2, **otros):
    print(param1)
    print(param2)
    for i in otros.items():
        print(i)

varios_dicc(1,2,tercero = 3)


print("-------------------------------")

# En python existen objetos inmutables como las tuplas
# por lo que si se intentan modificar una tupla pasado como 
# parámetro, lo que ocurrirá en realidad
# es que se crearía unaa nueva instancia

def f(x, y):
    x = x+3
    y.append(23)
    print(x,y)

x = 22
y = [22]
f(x,y)
print(x, y)

#Los enteros son inmutables, las listas son mutables

# en resumen, los valores mutables se comportan como	paso por referencia, y los
# inmutables como paso por valor

print("-------------------------------")

# para que una función pueda devolver un valor, se utiliza
# la palabra clave "return"

def sumar(x,y):
    suma = x + y
    return suma

# almacenamos el valor que devuelve en una variable
suma = sumar(3,4)

# imprimimos 
print("La suma es: " + str(suma))