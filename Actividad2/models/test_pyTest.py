# Con esta libreria realizaremos los tests
import pytest
import numpy as np

# Import las clases del archivo sobre el cual realizo las pruebas
from classifier import Classifier as csf

#---------------
#   GLOBAL SCOPE
#----------------
# Necesito generar algunas variables globales para poder utilizarlas en las funciones.
# Necesito tener los valores de X, Y sino no corre la funcion trainning
X, Y = csf.setUp()
# Creo una lista para recojer los elemento que me regresa la funcion trainning
dict = []
X_train, X_test, y_train, y_test = csf.training(X,Y)
dict =[X_train, X_test, y_train, y_test]
# Ingreso los datos de prueba para poder comprobar la funciones
testData = [[5.0, 3.3, 1.4, 0.2]]

#--------------------------·
#-- CAMBIO lo datos por el INPUT que recibo del usuario
#--------------------------·
# Entonces voy a inyectar estos datos con todos los demas dentro del algoritmo.
X_test = testData
# Guardo la prediccion en una variable
prediccion = csf.desicionClassifier(X_train, X_test, y_train, y_test)

#---------------
#   TEST 1
#----------------

def test_setUp():
    # Primero comprobamosque es la lista completa. El default de la variable global es 2 campos
    # Entonces si tiene mas de 5 campos si es
    assert len(Y) > 5

    # Comprobamos que la columna Y se comvirtio a nuemros desde 0 hasta 2 para poder hacer la prediccion
    assert min(Y) == 0
    assert max(Y) == 2

    # Comprobamos que X y Y son de tipo numpy array
    assert type(Y) == np.ndarray
    assert type(X) == np.ndarray

def test_trainning():
    # Aqui lo que busco es comprobar que todas los elementos son arrays
    for i in dict:
        assert type(i) == np.ndarray

    # Comprobamos que la columna y_train se comvirtio a nuemros desde 0 hasta 2 para poder hacer la prediccion
    assert min(dict[2])  == 0
    assert max(dict[2]) == 2

    # Comprobamos que la columna y_test se comvirtio a nuemros desde 0 hasta 2 para poder hacer la prediccion
    assert min(dict[3]) == 0
    assert max(dict[3]) == 2

def test_desicionClassifier():

    # La lista esta como un numpy array lo tengo que comvertir en lista para poder compararlo con los datos de prueba
    lista = prediccion.tolist()
    # Ordeno los resultados para poder compararlos como iguales
    lista.sort()

    # Me aseguro que tengan los mismo elementos
    assert len(lista) == len(testData)

    # me aseguro que ambos sean listas
    assert type(testData) == list
    assert type(lista) == list

    # Finalmente compara el resultado de la prediccion con los datos de prueba para saber si el algoritmo funciona
    assert lista == prediccion
