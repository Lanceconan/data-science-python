# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 23:39:40 2018

@author: Daniel
"""

import os

# Método para leer todos los archivos de un directorio
def knowFiles(directory):
    
    lstFiles = []
    arrayAllData = []
    lstDir = os.walk(directory)            
     
    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if(extension == ".csv"):
                lstFiles.append(nombreFichero+extension)
                arrayAllData.append(readFile(directory + '/' + nombreFichero + extension, 3))
                    
    return arrayAllData
    

# Método para leer datos de archivo y retorna un array 
# modo 1: Hombres
# modo 1: Mujeres
# modo 3: Combinado    
def readFile(addressFileYear, modo):
    nameArrayYear = []
    with open(addressFileYear, 'r') as fname:
        lines = fname.readlines()
        fileName, extension = os.path.splitext(addressFileYear)
        nameArrayYear.append(fileName)
        
        for line in lines:
            auxData = line.strip('\n').split(",")
            
            if(modo == 1):
                nameArrayYear.append(auxData[0].strip(' '))
            elif(modo == 2):
                nameArrayYear.append(auxData[1].strip(' '))
            else:    
                nameArrayYear.append(auxData[0].strip(' '))
                nameArrayYear.append(auxData[1].strip(' '))
    
    return nameArrayYear

# Método para leer una opción válida del teclado
def validateOption(option):
    try:
        return int(float(option))    
    except ValueError:        
        return -1 

# Método para validar el año ingresado es válido
def validateYear(year):    
    try:
        validYear = int(float(year)) 
        
        if(year >= 2002 and year <= 2015):
            return validYear
        else:
            return 0
    
    except ValueError:        
        return -1 
    

# Método para limpiar la pantalla
def cleanScreen():
    os.system('cls')

# Método que imprime el menú principal
def printMenu():    
    cleanScreen()

    print('Escoje una Opción')
    print('=================')
    print('1. TopFive Femenino por Año Ingresado (2002 - 2015) Gráfico PNG Incluido')
    print('2. TopFive Masculino por Año Ingresado (2002 - 2015) Gráfico PNG Incluido')
    print('3. TopFive Femenino de los nombres Históricamente más usados (2002 - 2015) Gráfico PNG Incluido')
    print('3. TopFive Masculino de los nombres Históricamente más usados (2002 - 2015) Gráfico PNG Incluido')
    print('4. Según el nombre ingresado revisar en que año fue el más popular y cuantos niños fueron llamados así')    
    print('')
    print('0. Salir')
    print('')

    return validateOption(input('Ingresa la opción que deseas descubrir: '))

#Método principal
def main():

    option = -1

    while(option != 0):
        
        option = printMenu()

        if(option == -1):
            cleanScreen()
            print('Opción no válida :(. Intenta algo válido ... :) ')
            input("\nTecla para continuar.... \n")

        elif(option == 0):
            cleanScreen()
            print('Has decidido irte de este super programa :(. Adios !!!! ')
            input("\nTecla para continuar.... \n")
        
        if(option == 1):
            print('opcion 1')
        
        elif(option == 2):
            print('opcion 2')
        
        elif(option == 3):
            print('opcion 3')
        
        elif(option == 4):
            print('opcion 4')




# Ejecutar el programa principal
#main()
#print(readFile('data/2005.csv', 1))
print(knowFiles('data/'))