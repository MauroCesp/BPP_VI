import pandas as pd
import os

# Esto lo importo para interactuar con la base de datos y sus metodos
# Menciono el directorio, el fichero y la clase dentro del fichero
from models.Operations import Statistics

from models.checks import Checks

#Con esta clase que hereda de Exceptions, puedo crear mis propias excepcciones
class misExcepciones(Exception):
    def __init__(self,valor):
        self.valorError = valor

class Finance:

  def securityCheck():
     try:
        #--------------------------------------------
        #           VERIFICACION 1
        #--------------------------------------------
        # Verifico si existe el aarchivo de esta manera
        # Compruebe que el fichero existe y que tiene 12 columnas, una para
        #cada mes del año
        Checks.exists()
        #--------------------------------------------
        #           VERIFICACION 2
        #--------------------------------------------
        # Lo primero que hay que hacer en un dataframe es limpiarlo de valore no presentes o incorrectos
        # Puedo llenar esos datos con valores por defecto tambien
        # El data frame ya limpio es lo que paso como parametro a los diferentes metodos
        df = Statistics.clean_data()
        #--------------------------------------------
        #           VERIFICACION 3
        #--------------------------------------------
        # Me aseguro que la el data set tenga clas 12 columnas
        cols = Checks.cols()
        if cols != 12:
            #Raise me sirve para lanzar mi propio error
            raise misExcepciones()
        else:
            return df, cols

     except misExcepciones:
        print('+---------------------------------------------------------------------------+')
        print("| No se puede trabajar con menos de 12 columnas, una para cada mes del año. |")
        print('+---------------------------------------------------------------------------+')

  def main(self):
    # COMPROBACIONES INICIALES ANTES DE COMENZAR
    df, cols = Finance.securityCheck()

    # Obtengo la seleccion del usuario
    x = Finance.menu()

    try:
        if x == 1:
            print('+----------------------------------+')
            print("| Estos son los datos del Data Set |")
            print('+----------------------------------+')
            print(df)
            print(' ')

        #---- GASTADO MAS
        elif x == 2:
            x = Statistics.min()
            print("| Mes en el que se ha gastado más: ",x)
            print('+----------------------------------+')
        #---- GASTADO MENOS
        elif x == 3:
            x = Statistics.max()
            print("| Mes en el que se ha gastado menos: ",x)
            print('+----------------------------------+')
        #---- GASTO TOTAL
        elif x == 4:
            x = Statistics.outcome()
            # Pongo la variable negativa para que el resultado sea positivo
            print("| El gasto total a lo largo del año: ", -x)
            print('+----------------------------------+')
        #---- INGRESO TOTAL
        elif x == 5:
            x = Statistics.income()
            print("| Ingreso total a lo largo del año:", x)
            print('+----------------------------------+')

        #---- MEDIA
        elif x == 6:
            x = Statistics.media()
            # Pongo la variable negativa para que el resultado sea positivo
            print("| La media de gasto es: ",-x)
            print('+----------------------------------+')

        #---- GRAFICO
        elif x == 7:
            Statistics.graph()

    except Exception as err:
        print(' Opss... Algo ha salido mal al ingresar los datos', err)

  def menu():
    print('+------------------------------------------------+')
    print('|                  ARCHIVO CSV                   |')
    print('+------------------------------------------------+')
    print('| 1   ----------- >  Mostrar archivo')
    print('| 2   ----------- >  ¿En qué mes se ha gastado más?')
    print('| 3   ----------- >  ¿En que més se ha gastado menos? ')
    print('| 4   ----------- >  ¿Cuál ha sido el gasto total a lo largo del año? ')
    print('| 5   ----------- >  ¿Cuáles han sido los ingresos totales a lo largo del año? ')
    print('| 6   ----------- > ¿Cuáles la media de gasto? ')
    print('| 7   ----------- > Grafico evolucion del ahorro en el año ')


    #----------------------------------------------
    # Recojo la informacion del usuario en un avariable1
    x = int(input(' Qué desea hacer? Escoja un número: '))
    print(' ')

    return x
#-------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------
#           INICIO DEL PROGRAMA
#--------------------------------------------

#---------------
# Creo el Objeto
#---------------
# Creo el Objeto para interactuar con la clase
o1 = Finance()
o1.main()
