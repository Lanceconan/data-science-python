import numpy as np
from numpy.random import randn

answer = None

x = randn()

if x < 1:
    answer = "Mayor que 1"
    print(answer)
else:
    answer = "Menor o igual que 1"
    print(answer)
        