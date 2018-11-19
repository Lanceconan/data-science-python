# -*- coding: utf-8 -*-

"""

Formato de Script de python
Para ejecutar

python script-avanzado.py argumento1, argumento2, argumento3, ..., argumenton

@autor Daniel Gutiérrez

"""

import argparse

def parseArguments():
    
    parser = argparse.ArgumentParser(
        description="Se describe que es lo que hace el script"
    )

    parser.add_argument(
        "metodo", 
        help="""
            Indica el metodo que se quiere usar.
            Valores válidos son saludar,felicitar
            """,  
        choices=["saludar", "felicitar"]
    ) 
 
    parser.add_argument(
        "usuario", 
        help="""
            Indica el usuario con quien se quiere interactuar.
            """
        )
 
    parser.add_argument(
        "--capitalizar", 
        help="Capitaliza el nombre del usuario",
        action="store_true"
    )
    
    argumentos = parser.parse_args()
    
    return argumentos


def main(argumentos):
    
    nombre = argumentos.usuario
    
    if argumentos.capitalizar:
        nombre = nombre.capitalize()
        print(nombre)
    
    if argumentos.metodo == "saludar":
        print("Hola ", nombre)
    
    elif argumentos.metodo == "felicitar":
        print("Felicidades ", nombre)
    
if __name__ == "__main__":
    
    # Este código solo se ejecutará si ejecutamos este script directamente
    argumentos = parseArguments()
    print("argumentos pasados al script: ", argumentos)
    main(argumentos)
