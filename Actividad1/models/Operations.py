import pandas as pd

# Importo este modulo para poder trabajar con el archivo que csv que me pasan y cambiar cosas
import csv
# importing statistics module
import statistics
import matplotlib.pyplot as plt
import numpy as np


class Statistics:
    global dictionary
    global value
    global key
    global df

    df = 'cleanedData.csv'
    df = pd.read_csv(df)
    # Creo una dict para guardar los valores totales de cada mes
    key = []
    value = []
    # Interactuo por cada coumna
    for name, values in df.iteritems():
        # Agrego la el total por mes a la lista con la funcion append
        key.append(name)
        value.append(df[name].sum())
        # Imprimo el total de cada mes
        #print("Total del mes de: ",name, df[name].sum())
    dictionary = dict(zip(key, values))

    def max ():
        #---- GASTADO MENOS
        # Encuentro el mes que tiene mas dinero
        # Es decir en el que menos se ha gastado
        gMinus = max(zip(dictionary.values(), dictionary.keys()))[1]
        # Use .items() to iterate over dataframe rows
        return gMinus

    def min ():
        gPlus = min(zip(dictionary.values(), dictionary.keys()))[1]
        return gPlus

    def media ():
        var = statistics.median(value)
        return var

    def income ():
        #---- GASTADO MAS
        # Para calcular los ingresos totales obtengo todos lso valores numericos del dataframe
        num = df._get_numeric_data()
        # Cualquier valor menor a = lo convierto en 0
        # Esto lo hago para obtener solo los valores positivos y poder sumarlos
        # Valores negativos fue dinero que salido# Valore positivos es dinero que entro
        num[num < 0] = 0

        #Guardo la informacion en un nuevo cvs para utilizarlo
        new1_file_csv = "income.csv"
        # CGuardo los datos en el nuevo fichero
        num.to_csv(new1_file_csv)

        # Calculo los ingresos totales a traves de la fucnion de numpy
        var = num.to_numpy().sum()
        return var

    def outcome():
        #---- GASTADO MAS
        # Para calcular los ingresos totales obtengo todos lso valores numericos del dataframe
        num = df._get_numeric_data()
        # Cualquier valor menor a = lo convierto en 0
        # Esto lo hago para obtener solo los valores positivos y poder sumarlos
        # Valores positivos fue dinero que entor# Valore negativos es dinero que salio
        num[num > 0] = 0

        #Guardo la informacion en un nuevo cvs para utilizarlo
        new1_file_csv = "outcome.csv"
        # CGuardo los datos en el nuevo fichero
        num.to_csv(new1_file_csv)

        # Calculo los ingresos totales a traves de la fucnion de numpy
        var = num.to_numpy().sum()
        return var


    def graph ():
        plt.bar(range(len(dictionary)), value, tick_label=key)
        plt.show()
    #----------------------------------------
    #----------   CLEAN DF   ----------------
    #-----------------
    #-----------------------
    # Recibo como parametro el data frame original
    def clean_data():
        file_csv = 'dataSet.csv'
        #----------------------------------------
        #----------   CLEAN MESSY DATA   --------
        #----------------------------------------
        new_file_csv = "cleanedData.csv"
        # Instead of directly replacing occurrences with the new character
        #(which may replace escaped occurrences of the character as well)
        # we can just use built-in functionality in the csv library to read the file for us
        # and then write it again
        with open(file_csv, newline='') as infile, open(new_file_csv, 'w', newline='') as outfile:
            # Leo el archivo y busco los delimitadores con el punto y coma
            reader = csv.reader(infile, delimiter='\t')
            # Ahora escribo en el nuevo archivo con el delimitador correcto
            writer = csv.writer(outfile, delimiter=',')

            # Inserto cada linea en el nuevo archivo
            for row in reader:
                writer.writerow(row)

        types = pd.read_csv(new_file_csv)

        return types, new_file_csv
