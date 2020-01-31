# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importando datos
dataset = pd.read_csv('Datasets/P4-Demographic-Data.csv')

#matriz de datos
x = dataset.iloc[:, -1].values
y = dataset.iloc[:, 3].values

