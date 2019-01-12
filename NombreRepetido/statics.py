# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 23:39:40 2018

@author: Daniel
"""

import os
from collections import Counter
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Método para dibujar un gráfico y guardarlo en la ubicación donde se ejecuta
def drawAndPrintGraphic(dataset, titlex, tittley):
    matplotlib.rcParams.update({'font.size': 18})
    ax = plt.gca()
    
    for i in range(10):
        ax.bar(i, np.random.randint(1000))

    plt.ylabel(tittley)
    plt.xlabel(titlex)
    plt.savefig("Ejemplo1.png")

# Método para leer todos los archivos de un directorio
def getDataFiles(directory):
    
    lstFiles = []
    arrayAllData = []
    lstDir = os.walk(directory)            
     
    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if(extension == ".csv"):
                lstFiles.append(nombreFichero + extension)
                arrayAllData.append(readFile(directory + '/' + nombreFichero + extension, 3))
                    
    return arrayAllData
    
# Método para estandarizar el separador de las linea extraidas desde los csv
def standarizeLine(line):
    replacements = (',', ';')
    for r in replacements:
        line = line.replace(r, ';')
    
    return line.strip('\n').split(";")

# Método para leer datos de archivo 
# Retorna un array con todo los nombres según sea el caso
#
# modo 1: Hombres
# modo 1: Mujeres
# modo 3: Combinado    
def readFile(addressFileYear, modo):
    nameArrayYear = []
    with open(addressFileYear, 'r') as fname:
        lines = fname.readlines()
        fileName, extension = os.path.splitext(addressFileYear)
        nameArrayYear.append(fileName[-4:])
                
        for line in lines:
            auxData = standarizeLine(line)            
                        
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

# Método para validar la entrada de un nombre
def validateName(name):
    return name.isalpha()    

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
    print('4. Mostrar en que año según el nombre ingresado fue el más popular y cuantos niños fueron llamados así')
    print('5. Mostrar cuantos niños por año fueron llamados según un nombre ingresado')  
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
            input("\nTecla para continuar.... \n")
        
        elif(option == 2):
            print('opcion 2')
            input("\nTecla para continuar.... \n")
        
        elif(option == 3):
            print('opcion 3')
            input("\nTecla para continuar.... \n")
        
        elif(option == 4):
            print('opcion 4')
            cleanScreen()
            namesByYear = getDataFiles('data/')    
            name = input('ingresa un nombre para saber cuando fue el más popular: ')          
            name = name.upper()            
            varcounter = 0
            varyear = 0
            
            if(validateName(name)):                
               
                for nameunit in namesByYear:
                    countNames = Counter(nameunit)
                    
                    if(countNames[name] > varcounter):
                        varyear = nameunit[0]
                        varcounter = countNames[name]

                if(varyear == 0 or varcounter == 0):
                    print('')    
                    print('el nombre ' + name + ' no existe en los registros de los archivos')
                else:
                    print('')    
                    print('ha sido en el año ' + str(varyear) + ' el nombre ' + name + ' el más popular con ' +  str(varcounter) + ' registros')

                input("\ntecla para continuar.... \n")
            else:
                print('no es un nombre válido')
                input("\ntecla para volver al menú principal .... \n")

        elif(option == 5):
            print('opcion 5')
            input("\nTecla para continuar.... \n")





# Ejecutar el programa principal
main()