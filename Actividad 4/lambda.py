# COnocidas como funciones anonimas porque se definen sin un nombre
# SIntaxis de una funcion lambda

# lambda parametros : expresion
# Funciones puede definir cualquier numero de parametros pero solo una expresion
# Se utiliza en combinacion de otras Funciones
# Esta funcion no tinen nombre y se la asignadmos a una variable
cuadrado = lambda x : x**2

"""
def cuadrado(x):
    return x**2
"""
#Para utilizar la funcion llamamos  a la funcion y le pasamos los parametros.
print(cuadrado(2))

#####
# MAP
#####

#Aplica un FUNCION a cada uno de los elementos de una lista
# map( una funcion , una lista)
enteros = []

# Ponemos list para recuperar los valores de todas las funciones sino solo nos pasa unos interadores
cuadrados = list(map(lambda x:x**2,enteros))

# Podemos tener listas de funciones
# Creamos dos funciones
def cuadrado():
    return x**2

def cubo():
    return x**3

# Creamos una lista para guardar nuestras funciones
funciones = [cuadrado,cubo]
# Necesito un cilo for para ejecutar las funciones a cada valor dentro de las listas
# Es de cir cada fucnion
for e in enteros:
    valores = list (map(lambda x : x(e), funciones))
    print(valores)

############
# FILTER
#################
# Filtrar lista de elementos a lo que el resultado es True

# filter(una funcion , una lista)

valores =[1,2,3,4,5]

# Lambda le pasamos (parametro, expresion)
# Al mismo tiempo LAMBDA es el parametro para FILTER
# Aqui le sacamos el modulo de 2
pares = list(filter(lambda x : x%2 == 0, valores))

# Reduce
# import functools
# O de forma mas optimizada
# fromfunctools import Reduce
# Lambda le pasamos dos parametros(acepta cuantos queramos) pero una unica expresion
# El el caso de reduce estamos oblogados a trabajar con ddos parametros
# Lambda hace un calculo acumulativo sobre una lista de valores
# Dedicamos un parametro para guardar el acumulativo
# Otro para guardar los valores de los elementos de la lista
#suma = reduce(lambda x, y)
suma = reduce(lambda x, y:x+y, valores)
