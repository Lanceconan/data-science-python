"""

Crear un diccionario cuyas claves sea los tres primeros días de la semana ylos valores sean la posición de ese día dentro de la semana

"""

diccionarioDias = {
    "Lunes": 1,
    "Martes": 2,
    "Miercoles": 3,
    "Jueves": 4,
    "Viernes": 5,
    "Sábado": 6
}

print(diccionarioDias);

diccionarioDias["Domingo"]  = 7

print(diccionarioDias);


"""

Pasar a mayúscula los días de la semana añadidos al diccionario

"""

diccionarioDias["LUNES"] = diccionarioDias.pop("Lunes")
diccionarioDias["MARTES"] = diccionarioDias.pop("Martes")
diccionarioDias["MIERCOLES"] = diccionarioDias.pop("Miercoles")
diccionarioDias["JUEVES"] = diccionarioDias.pop("Jueves")
diccionarioDias["VIERNES"] = diccionarioDias.pop("Viernes")
diccionarioDias["SABADO"] = diccionarioDias.pop("Sábado")
diccionarioDias["DOMINGO"] = diccionarioDias.pop("Domingo")

print(diccionarioDias);

"""

Pasar a minúscula todas las palabras del diccionario

"""

for nombre, dia in diccionarioDias.items():
    print (nombre, dia)
    diccionarioDias[nombre.lower()] = diccionarioDias.pop(nombre)

"""

Obtener una lista de los días que contienen una O

"""
listaDias = []
for nombre, dia in diccionarioDias.items():
    if ('O' in nombre or 'o' in nombre):
        print(nombre)
        listaDias.insert(len(listaDias), nombre)

print('Lista de días: ', listaDias)


"""

Funciones para operaciones entre dos valores

"""

def sumar(n1, n2):
    return n1 + n2


def restar(n1, n2):
    return n1 - n2


def multiplicar(n1, n2):
    return n1 * n2


def dividir(n1, n2):
    if(n2 == 0):
        print('No se puede dividir por cero')
        return 'Inf'
    
    return n1 / n2

def allInclusive(n1, n2):
    suma = n1 + n2
    resta = n1 - n2
    multiplicacion = n1 * n2
    
    if(n2 == 0):
        print('No se puede dividir por cero')
        division = 'Inf'
    else:
        division = n1 / n2

    return suma, resta, multiplicacion, division

sumaLambdaFunc = lambda n1, n2: n1 + n2;
toUpperLambdaFunc = lambda text: text.upper();

# uso de las funciones
while(1 == 1):
    try:
        n1 = input('Ingresa un primer número entero a operar matemáticamente: ')
        n1 = float(n1)
        n2 = input('Ingresa un segundo número entero a operar matemáticamente: ')
        n2 = float(n2)

        print('')
        print('La suma es: ', sumar(n1, n2))
        print('La resta es: ', restar(n1, n2))
        print('La multiplicacion es: ', multiplicar(n1, n2))
        print('La división es: ', dividir(n1, n2))

        print('')
        suma, resta, mult, div = allInclusive(n1, n2) 

        print('La suma todo en uno es: ', suma)
        print('La resta todo en uno es: ', resta)
        print('La multiplicacion todo en uno es: ', mult)
        print('La división todo en uno es: ', div)

        print('')
        sumaLambda = sumaLambdaFunc(n1, n2)
        print('La suma Lambda es: ', sumaLambda)

        text = str(input('Texto a mayusculas con lambda: '))
        print ('El texto es: ', toUpperLambdaFunc(text))
        break;

    except ValueError:
        print("No es un numero entero")
        input("\nTecla para continuar.... \n")  

"""

CREAR UN OBJETO DE LA CLASE INSTRUMENTOS

"""
import Instrumento
import Newton

guitarra = Instrumento.Instrumento(10, 10, 10, 10, False);

competidor1 = Newton.Newton(0, 220, 0, 150, 450)

print('')
print('La energía cinética es: ', competidor1.energiaCinetica())
print('La energia potencial es: ', competidor1.energiaPotencial())
print('La distancia recorrida es: ', competidor1.distancia())
print('La aceleración es: ', competidor1.aceleracion())
print('La fuerza es: ', competidor1.fuerza())
