# Importo la libreria para trabajar con objetos json
# Con jsonify podemos pasar de un diccionario a un objeto json
# Las APIs generalmente trabajan con objetos json
# COn request me permite hacer los POST-GET
import pandas as pd
import csv
# Esto lo importo para interactuar con la base de datos y sus metodos
# Menciono el directorio, el fichero y la clase dentro del fichero
# Este es el modelo que cree para realizar las predicciones
from models.classifier import Classifier as pred
from models.raiseExceptions import myExceptions as ex


class Iris:

    #---------------
    #    GET DATA
    #----------------
    def menu(*args):
        print('+------------------------------------------------+')
        print('|                  IRIS DATA SET                 |')
        print('+------------------------------------------------+')
        print('| 1   ----------- >  Mostrar archivo')
        print('| 2   ----------- >  Predicción')
        print()
        #----------------------------------------------
        # Recojo la informacion del usuario en un avariable1
        x = int(input(' Qué desea hacer? Escoja un número: '))
        print(' ')

        if x == 1:
            Iris.irisData()

        elif x == 2:
            Iris.predictData()
        else:
            raise ex("Por favor escoja una de las opciones disponibles.")

    #---------------
    #    GET DATA
    #----------------
    def irisData():
        df = pd.read_csv("iris.csv")
        # axos='columns' to count with respect to row
        count = int(len(df))
        print('+------------------------------------------------+')
        print('|                  IRIS DATA SET                 |')
        print('+------------------------------------------------+')
        print()
        # Paso el count de los elementos dentro del data y el dataset completo
        print("Este Dta set contiene: ",count," registros")
        print('+------------------------------------------------+')
        print()
        print(df)
    #---------------
    #    PREDICT
    #----------------

    def predictData():
        print('+------------------------------------------------+')
        print('|                  IRIS DATA SET                 |')
        print('+------------------------------------------------+')
        print()
        print("Ingrese los datos de la predicción: ")
        print('+------------------------------------------------+')
        print()
        sl = input('Sepal Length: ')
        sw = input('Sepal Width: ')
        pl = input('Petal Length: ')
        pw = input('Petal Width: ')
        print('+------------------------------------------------+')
        print()

        #--------------------------·
        #-- INYECTO datos
        #--------------------------·
        # convierto los datos en una lista para inyectarlo en la funcion
        # como un X_test una vez que el modelo esta entrenado
        testData = [[sl, sw, pl, pw]]

        print("Sobre estos datos se realizará la predicción: ", testData)
        print('+------------------------------------------------+')
        print()

        # Llamo a mi metodo de desicionclassifier en el modelo de classifier
        # Obtengo las valieables para entrenar mi MODELO
        # Llamo directamente porque setup, trainig  los  llamo dentro del metodo
        X, Y = pred.setUp()

        X_train, X_test, y_train, y_test = pred.training(X,Y)
        #--------------------------·
        #-- CAMBIO lo datos por el INPUT que recibo del usuario
        #--------------------------·
        # Entonces voy a inyectar estos datos con todos los demas dentro del algoritmo.
        X_test = testData

        # Guardo la prediccion en una variable
        prediccion = pred.desicionClassifier(X_train, X_test, y_train, y_test)

        # Como tengo el eje Y  convertido en numeros lo debo de pasar a string
        # COn un bucle if analizo el retorno de la funcion
        print('+-------------+')
        print('|  Resultado  |')
        print('+-------------+')
        print()
        try:
            if prediccion == 0:
                print(' Según los datos la especie es: SETOSA')
            elif prediccion == 1:
                print('Según los datos la especie es: VERSICOLOR')
            else:
                print('Según los datos la especie es: VIRGINICA')
        except Exception as err:
            print(' Upss... Algo ha salido mal con tu predicción --->', err)

#--------------------------------------------
#           INICIO DEL PROGRAMA
#--------------------------------------------

#---------------
# Creo el Objeto
#---------------
# Creo el Objeto para interactuar con la clase
obj = Iris()
obj.menu()
