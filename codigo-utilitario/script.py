# -*- coding: utf-8 -*-

"""

Formato de Script de python
Para ejecutar

python script.py argumento1, argumento2, argumento3, ..., argumenton

@autor Daniel Gutiérrez

"""

import sys

# Importar los argumentos brindados al script
def parseArguments():
    arguments = sys.argv[1:]
    return arguments

# Método principal, aquí va todo el modulo fuente
def main(argumentos):
    print("Otra vez los Argumentos, solo el primero: ", argumentos[0])

# Bloque de código que se ejecuta por primera vez
if __name__ == "__main__":
    arguments = parseArguments()
    print("Los argumentos que le dimos son: ", arguments)
    main(arguments)
