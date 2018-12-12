# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 21:26:00 2018

@author: Daniel

"""

import os
from collections import deque

turno = deque(["O", "X"])

tableroPosiciones = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]

tableroJuego = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
]

def translatePosition(position):
    if(any(position in arr for arr in tableroPosiciones)):
        for i in range(3):
            for j in range(3):
                if(position == tableroPosiciones[i][j]):                    
                    return i, j;        
        return -1, -1                
    else:
        return -1, -1
    #return tableroPosiciones.index(position)
        
def printTablero(tablero):
    print(tablero[0])
    print(tablero[1])
    print(tablero[2])

def printMenuJuego():
    os.system("clear")
    print("Tablero de Posiciones")
    print("=====================")
    printTablero(tableroPosiciones)
    print('')
    print("Tablero de Juego")
    print('=================')
    printTablero(tableroJuego)
    print('')
    
def isWinner():    
    return False;
    
def play(x, y, player):
    tableroJuego [x][y] = player;
    changeTurn()
    
  
def isOcuppied(x, y):    
    return tableroJuego[x][y] != ''
    
def changeTurn():
    turno.rotate()
    return turno[0]

#Método para leer la posición de la Jugada
def readPosition(player):
    pivote = 0
    
    while(pivote == 0):
        
        try:
            printMenuJuego()
            n = input('Turno: ' + player + ' - Ingresa tu posición para Jugar: ')
            n1 = int(float(n))            
            
            x, y = translatePosition(n1)
            
            if(x == -1 and y == -1):                
                print("No es una posición válida de juego")
                input("Tecla para continuar....")                
                pivote = 0
            
            elif(isOcuppied(x, y) == False):
                pivote = 1
            
            else:            
                print('Esa posición está ocupada ahora. Intenta otra ...')
                input("Tecla para continuar....")                
                pivote = 0
                
        except ValueError:
            print("Lo que tecleaste no es un número. Intenta con una posición Libre ...")
            input("Tecla para continuar....")            
            
    return x, y

    
def main():
    
    while(isWinner() == False):        
        x, y = readPosition(turno[0])
        play(x, y, turno[0])


# Ejecución de Método pricipal
main();

    
    

