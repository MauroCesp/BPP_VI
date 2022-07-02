################
# FILTER
#################
# Filtrar lista de elementos a lo que el resultado es True

# filter(una funcion , una lista)

valores = [3, 4, 8, 5, 5, 22, 13]

# Lambda le pasamos (parametro, expresion)
# Al mismo tiempo LAMBDA es el parametro para FILTER
# Aqui le sacamos el modulo de 2
primos = list(filter(lambda x : x%2 != 0, valores))
print(primos)
