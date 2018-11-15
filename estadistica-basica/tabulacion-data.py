"""
Dependencias  a instalar:


Ejecutar:
$ py tabulacion-data.py

"""
# IMPORTAR LIBRERIAS
import random
import os 
import collections
import numpy as np

# METODOS A UTILIZAR DURANTE LA EJECUCIÓN DEL PROGRAMA

# Método para crear una lista de datos aleatoria
def setRandomList(n):
    lista = []

    for i in range(n):
        lista.insert(i, random.randrange(0, 100, 1))

    return lista

# Método para ordenar una lista
def orderList(listaData):
    return sorted(listaData)

# Método para calcular la media aritmética de la variable
def calculateMediaAritmetica(listaDataSorted):
    return 0

# Metodo para calcular la media geométrica de la variable
def calculateMediaGeometica(listaDataSorted):
    return 0

# Metodo para calcular la media Armonica de la variable
def calculateMediaArmonica(listaDataSorted):
    return 0

# INICIO DE PROGRAMA

opcion = 0
listaData = []
listaDataSorted = []

while (opcion != 5):

    os.system('cls')
    print("TABULACIÓN DE DATOS DE VARIABLES CUANTITATIVAS")
    print("================================\n")
    print("1. DISCRETA")
    print("2. CONTÍNUA")
    print("3. SALIR")

    opcion = int(input("Ingresa tu opción: "))
    os.system('cls')

    if(opcion == 1):

        n = 0
        while(n < 9): #debe ser 99
            os.system('cls')
            print("SE TRABAJARAN CON VARIABLES CUANTITATIVAS DISCRETAS")
            print("====================================================\n\n")


            try:
                n = int(input("Ingresa la cantidad de observaciones aleatorias discretas a generar: "))

                if(n < 10): #debe ser 10
                    print("El número que ingresas debe ser mayor o igual 100")     
                    input("\nTecla para continuar.... \n") 
               
            except ValueError:
                print("No es un numero entero")
                input("\nTecla para continuar.... \n")  
        
        listaData = setRandomList(n)
        listaDataSorted = orderList(listaData)

        print("\nLa lista generada es: \n\n", listaData)
        print("\nLa lista ordenada es: \n\n", listaDataSorted)

        print("\nLa media aritmetica es: ", calculateMediaAritmetica(listaDataSorted))
        print("La media geometrica es: ", calculateMediaGeometica(listaDataSorted))
        print("La media armónica es: ", calculateMediaArmonica(listaDataSorted))
        print("La moda es: ", np.mean(listaDataSorted))
        print("La mediana es: ", np.median(listaDataSorted))
        
        frequences = collections.Counter(listaDataSorted)

        print("\n\n Cambiar ... Counter: \n\n", frequences) 

        print("Diccionario: \n\n", frequences)
        print("\nKeys: \n\n", frequences.keys())
        print("\nValues: \n\n", frequences.values())

        input("\nTecla para continuar.... \n") 

    elif (opcion == 2):
        print("ESCRIBIRÁ NUEVO REGISTRO EN LA BASE")
        print("===================================\n\n")
       

        input("\nTecla para continuar.... \n")     
        
    elif (opcion == 3):
        print("TERMINASTE LA EJECUCIÓN DEL PROGRAMA") 
        break
    
    else:
        print("OPCION NO VÁLIDA") 
        input("\nTecla para continuar.... \n")

# FIN DE PROGRAMA
