# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

# conda install numpy
# conda install pandas
# conda install matplotlib
# pip install sklearn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importando datos
dataset = pd.read_csv('Datasets/P4-Demographic-Data.csv')

#matriz de datos
x = dataset.iloc[:, -1].values
y = dataset.iloc[:, 3].values

#Datos Faltantes

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = 'Nan', strategy='mean', axis=0)
imputer = Inputer.fit(x[:2:4])
x[:,1:3] = imputer.transform()

