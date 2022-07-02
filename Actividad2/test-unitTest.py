from models.classifier import Classifier as csf
import unittest
import numpy as np

#--------------------------------------------------------------------
#                   CLASE OPS
#--------------------------------------------------------------------
# En esta clase guardo las operaciones que voy a repetir
class Ops():
    def xandy():
    # Necesito generar algunas variables globales para poder utilizarlas en las funciones.
    # Necesito tener los valores de X, Y sino no corre la funcion trainning
        X, Y = csf.setUp()
        return X, Y

    def training():
        X, Y = Ops.xandy()
        # Creo una lista para recojer los elemento que me regresa la funcion trainning
        dict = []
        X_train, X_test, y_train, y_test = csf.training(X,Y)
        dict =[X_train, X_test, y_train, y_test]
        return dict, X_train, X_test, y_train, y_test

    def prediccion():
        dict, X_train, X_test, y_train, y_test = Ops.training()
        # Ingreso los datos de prueba para poder comprobar la funciones
        testData = [[5.0, 3.3, 1.4, 0.2]]
        #--------------------------·
        #-- CAMBIO lo datos por el INPUT que recibo del usuario
        #--------------------------·
        # Entonces voy a inyectar estos datos con todos los demas dentro del algoritmo.
        X_test = testData
        # Guardo la prediccion en una variable
        prediccion = csf.desicionClassifier(X_train, X_test, y_train, y_test)
        return testData, prediccion

#--------------------------------------------------------------------
#                   CLASE TestEjemplos
#--------------------------------------------------------------------
class TestEjemplos(unittest.TestCase, Ops):

    def test_vars(self):
        # Llamo a mi clase Ops para utilizar sus metodos
        X,Y = Ops.xandy()
        print("Entra en el setup")
        # .assertEqual(a, b): Verifica la igualdad de ambos valores.
        # Primero comprobamosque es la lista completa. El default de la variable global es 2 campos
        # Entonces si tiene mas de 5 campos si es
        #assert len(Y) > 5

        # Comprobamos que la columna Y se comvirtio a nuemros desde 0 hasta 2 para poder hacer la prediccion
        # min(Y) == 0
        self.assertEqual(min(Y),0)
        self.assertEqual(max(Y),2)

        # Comprobamos que X y Y son de tipo numpy array
        #assert type(Y) == np.ndarray
        #assert type(X) == np.ndarray

    def test_trainning(self):
        # Llamo a mi clase Ops para utilizar sus metodos
        dict, X_train, X_test, y_train, y_test = Ops.training()
        # Aqui lo que busco es comprobar que todas los elementos son arrays
        for i in dict:
            self.assertIs(type(i),np.ndarray)

        # Comprobamos que la columna y_train se comvirtio a nuemros desde 0 hasta 2 para poder hacer la prediccion
        self.assertEqual(min(dict[2]),0)
        self.assertEqual(max(dict[2]),2)

        # Comprobamos que la columna y_test se comvirtio a nuemros desde 0 hasta 2 para poder hacer la prediccion
        self.assertEqual(min(dict[3]),0)
        self.assertEqual(max(dict[3]),2)

    def test_desicionClassifier(self):

        # La lista esta como un numpy array lo tengo que comvertir en lista para poder compararlo con los datos de prueba
        testData, prediccion = Ops.prediccion()

        # La lista esta como un numpy array lo tengo que comvertir en lista para poder compararlo con los datos de prueba
        lista = prediccion.tolist()
        # Ordeno los resultados para poder compararlos como iguales
        lista.sort()

        # Me aseguro que tengan los mismo elementos
        self.assertEqual (len(lista),len(testData))

        # me aseguro que ambos sean listas
        self.assertEqual (type(testData),list)
        self.assertEqual (type(lista),list)

if __name__ == '__main__':
    unittest.main()

# El test se corre python -m unittest -v <nomre del archivo>

# .assertEqual(a, b): Verifica la igualdad de ambos valores.
# .assertTrue(x): Verifica que el valor es True.
# .assertFalse(x): Verifica que el valor es False.
# .assertIs(a, b): Verifica que ambas variables son la misma (ver operador is).
# .assertIsNone(x): Verifica que el valor es None.
# .assertIn(a, b): Verifica que a pertenece al iterable b (ver operador in).
# .assertIsInstance(a, b): Verifica que a es una instancia de b
# .assertRaises(x): Verifica que se lanza una excepción.
