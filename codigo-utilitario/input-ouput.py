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


# leer la linea de un archivo con mayor longitud

def leerLineaMayorLongitud(archivo):
    lineaMayor = ''
    longitudLineaMayor = 0

    with open(archivo, "r") as fname:
        lineas = fname.readlines()
        for linea in lineas:
            if(len(linea) > longitudLineaMayor):
                lineaMayor = linea
                longitudLineaMayor = len(linea)
    
    return lineaMayor

carpetaLectura = Path("./data/")
archivoLectura = carpetaLectura / "datos.csv"

print("La mayor Linea es: ", leerLineaMayorLongitud(archivoLectura))

# Método para leer las últimas n lineas
def leerEneLineas(archivo, n):
    nlineas = []
    with open(archivo, "r") as fname:
        lineas = fname.readlines()        
        cardinal = len(lineas)    
        tope = cardinal - n    
        while(tope <= cardinal):
            nlineas.append(lineas[tope-1])
            tope+=1
            

    return nlineas

carpetaLectura = Path("./data/")
archivoLectura = carpetaLectura / "datos.csv"
print(leerEneLineas(archivoLectura, 100))


diccionarioEjercicio = {
    "nombre"    : ["Daniel", "Samuel", "Gustavo",  "Eduardo", "Guillermo"],
    "edad"      : [28, 25, 29, 28, 29],
    "ciudad"    : ["Calama", "Valdivia", "Antofagasta", "Copiapo", "Quintero"]
}

def escribirCsvFromDiccionario(archivo, diccionario):
    
    with open(archivo, "w") as fname:
        columns = list(diccionario.keys())
        valueRows = list(diccionario.values())
        
        
        for column in columns:
            fname.write(column)
            fname.write(',')
        
        fname.write('\n')
        
        pivote = 0
        while(pivote < len(valueRows[0])):
            pivote2 = 0
            while(pivote2 < (len(columns))):
                print(": ", valueRows[pivote2][pivote])
                fname.write(str(valueRows[pivote2][pivote]))
                fname.write(',')
                pivote2+=1         

            pivote2 = 0
            fname.write('\n')    

            pivote += 1

    return True

print("")
print("")
carpetaEscritura = Path("./data/")
archivoEscritura = carpetaEscritura / "misAmigos.csv"

print("")
if(escribirCsvFromDiccionario(archivoEscritura, diccionarioEjercicio)):
    print("Es escribió el archivo: ", archivoEscritura)
else:
    print("Ocurrió un error y no se escribió nada")

