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