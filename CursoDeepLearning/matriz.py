import numpy as np

myData = np.arange(0, 20)


Matriz1 = np.reshape(myData, (5, 4), order = 'C') # IMPRIME MATRIZ HORIZONTAL
print(Matriz1)

print ("")
Matriz2 = np.reshape(myData, (5, 4), order = 'F') # IMPRIME MATRIZ VERTICAL
print(Matriz2)

print("")

print("Elemento [2][0] es: ", Matriz1[2,0])

# ARRAY CON NUMPY

r1 = ["Hola", "es un", "dia bueno!"]
r2 = [3, 4, 5]
r3 = [2.3, 3.5, 4.5]

var = [r1, r2, r3]

print("")
print(np.array(var))