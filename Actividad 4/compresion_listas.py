cuadrados = [i **2 for i in range(5)]
print(cuadrados)

"""
cuadrados1 = []
for i in range(5):
    cuadrados1.append(i**2)
print(cuadrados)
"""


# STRINGS
frase = "Hola Mundo"

letras_o= [i for i in frase if i == 'o']
print(letras_o)


def al_cuadrado(i):
    retuurn i**2
cuadrado2 = [alcuadrado]

# COmpresion de conjuntos
lista1 = [1,2,3]
liasta2 = ["a","b","c"]

mi_dic = {i:j for i,j in zip(lista1,lista2)}

print(mi_dic)
