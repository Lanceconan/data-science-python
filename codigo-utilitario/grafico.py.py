# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

"""
import numpy as np 
import matplotlib.pyplot as plt

data = np.loadtxt(['1','2','3', '1', '2', '1', '2', '1', '1', '2', '2', '2', '2', '2', '2', '2', '2','2' ,'2' ])
hist, bin_edges = np. histogram(data, 10)
plt.hist(data, bins=bin_edges)
plt.show()

"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size': 21})
ax = plt.gca()

ax2 = ax.twinx()
for i in range(10):
    ax.bar(i, np.random.randint(1000))

plt.ylabel('Datos')
plt.savefig("Ejemplo1.png")