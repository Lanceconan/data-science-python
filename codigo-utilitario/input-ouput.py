import os

# crear carpeta
os.makedirs("./data/", exist_ok = True)

# escribir archivo
archivoNuevo = open("./data/prueba.txt", "a")
archivoNuevo.writelines("Linea 1")
archivoNuevo.writelines("Linea 2")
archivoNuevo.close()

# leer archivo
nombreArchivos = []

with open("./data/datos.csv", "r") as fname:
    lineas = fname.readlines()
    for linea in lineas:
        nombreArchivos.append(linea.strip("\n").split(","))

print(nombreArchivos)

# uso de pathlib - escribir archivo
from pathlib import Path

otrosNombres = ['Daniel', 'Valentina']

carpeta = Path("./data/")
archivo = carpeta / "datos.csv"

with open(archivo, "a") as fname:
    for nombre in otrosNombres:
        fname.write(nombre)
        fname.write("\n")

# uso de pathlib - leer archivo

carpeta = Path("./data/")
archivo = carpeta / "datos.csv"

print(archivo.read_text())





