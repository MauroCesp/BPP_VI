import pandas as pd
import os

# Importo este modulo para poder trabajar con el archivo que csv que me pasan y cambiar cosas
import csv


class Checks:

    # Declaro el archivo que voy a leer
    def exists():
        try:
            dataSet = 'dataSet.csv'
            df= pd.read_csv(dataSet)
        except Exception as er:
            print(' Opss... Existe el siguiente problema: ', er)

#------------------------------------------------
    def cols():
        try:
            dataSet = 'cleanedData.csv'
            df= pd.read_csv(dataSet)
            x = len(df.columns)
            return x
        except Exception as er:
            print(' Opss... Existe el siguiente problema: ', er)
