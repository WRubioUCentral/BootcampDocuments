import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter
import seaborn as sns
import io
import base64

# Trae dataframe desde Kaggle
def cargaKaggle(self, usuario, data):
            """
            Usuario: usuario de Kaggle.
                Ejemplo: https://www.kaggle.com/datasets/williamrrubio/data-siniestros-bogot-2015-2021/Data_completa.csv
                En esta dirección el usuario es williamrrubio/data-siniestros-bogot-2015-2021
            Data: solicita el nombre del documento
                Ejemplo: Data_completa.csv

            Retorna el Dataframe con la información solicitada
            """
            file_path = data
            df = kagglehub.load_dataset(KaggleDatasetAdapter.PANDAS,usuario,file_path,)
            df.head()
            return df
        
# Trae dataframe desde GitHub
def cargaGit(self, url):
            """
            url: Ruta de GitHub donde se encuentra el dataframe
            """
            df = pd.read_csv(url)
            df.head()
            return df 