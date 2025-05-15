import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter
import seaborn as sns
import io
import base64

def dispersion(self, dataframe, col1, col2):
            """
            Esta función pretende devolver la imágen de la gráfica solicitada en formato png
            
            Parámetros de entrada:
                Dataframe
                Nombre de columna 1
                Nombre de columna 2
            """
            plt.plot(dataframe[col1], dataframe[col2])
            plt.xlabel(f"{col1.capitalize()}")
            plt.ylabel(f"{col2.capitalize()}")
            plt.grid()
            plt.title(f"{col1.capitalize()} vs {col2.capitalize()}")
            ##Guardamos el gráfico
            buf = io.BytesIO()
            plt.savefig(buf, format = "png")
            buf.seek(0)
            img = base64.b64encode(buf.getvalue()).decode('utf8')
            return img
        
def dispersion(self, dataframe, col):
            """
            Esta función pretende devolver la imágen de la gráfica solicitada en formato png
            
            Parámetros de entrada:
                Dataframe
                Nombre de columna a graficar
            """
            plt.plot(dataframe[col])
            plt.ylabel(f"{col.capitalize()}")
            plt.grid()
            plt.title(f"{col.capitalize()}")
            ##Guardamos el gráfico
            buf = io.BytesIO()
            plt.savefig(buf, format = "png")
            buf.seek(0)
            img = base64.b64encode(buf.getvalue()).decode('utf8')
            return img
        
def histograma(self, dataframe, col, columnas = 7):
            """
            Esta función devuelve el histograma con 7 columnas por defecto

            Parámetros de entrada:
                Dataframe
                Nombre de la columna a graficar
                Cantidad de columnas
            """
            plt.hist(dataframe[col], bins = columnas)
            plt.xlabel(f"{col.capitalize()}")
            plt.ylabel("Frecuencia")
            plt.title(f"Histograma de {col.capitalize()}")