"""

SETS Y TRABAJOS CON SETS

"""

amigosCasa = set(["Juan Manuel", "Sebastian", "Bryan", "Fabian"])
amigosU = set(["Juan Manuel", "Nelson", "Ricardo"])

amigosCasa.add("Sergio")
amigosU.add("Oscar")
amigosCasa.remove("Bryan")

todosAmigos = amigosCasa.union(amigosU)
amigosComun = amigosCasa.intersection(amigosU)
amigosExclusivosCasa = amigosCasa - amigosU
amigosExclusivosU = amigosU - amigosCasa

print("Todos mis amigos son: ",  todosAmigos)
print("Amigos en Comun son: ", amigosComun)
print("Amigos Exclusivos de la Casa: ", amigosExclusivosCasa)
print("Amigos Exclusivos de la Universidad: ", amigosExclusivosU)

numeros = [1,2,1,2,1,2,3,3,3,3,4,4,1,5,2,5,2]
numerosUnicos = list(set(numeros))

print("")
print("Los únicos números son: ", numerosUnicos)

"""

USO DE COUNTER

"""
from collections import Counter

nombresRegistros = [
    "Daniel",
    "Valentina",
    "Daniel",
    "Valentina",
    "Daniel",
    "Valentina",
    "Daniel",
    "Valentina",
    "Valentina",
    "Valentina",
    "Daniel",
    "Valentina",
    "Valentina",
    "Valentina",
    "Daniel",
    "Valentina",
    "Valentina",
    "Valentina",
    "Valentina",
    "Valentina",
    "Daniel",
    "Valentina"    
];

counter = Counter(nombresRegistros)

print("")
print("Resumen de Registros: ", counter)

print("Valentina son: ", counter["Valentina"])
print("Daniel son: ", counter["Daniel"])

counter.update({"Daniel" : 7, "Valentina": 7, "Julio": 2})
counter["Matias"] = 15

print("")
print("Actualizados")
print("Resumen de Registros: ", counter)

print("Valentina son: ", counter["Valentina"])
print("Daniel son: ", counter["Daniel"])
print("Matias son: ", counter["Matias"])
print("Julio son: ", counter["Julio"])

"""

DefaultDict

"""

from collections import defaultdict

saboresHelado = defaultdict(lambda: "vainilla")
print("")
print("")
print('Sabores de Helados: ', saboresHelado)

saboresHelado["Manuel"] = "chocolate"
saboresHelado["Maria"] = "menta"

print('Sabores de Helados: ', saboresHelado)
print('Sabor de Helado de Juan: ', saboresHelado["Juan"])
galletaSet = {"Vino" : "McKay", "Morocha": "Fruna"}
galleta = defaultdict(lambda: "Trendy", galletaSet)

print("")
print("Las galletas son: ", galleta)

pokemon_entrenadores_lista = [
    ["Ash", "Nidorina"],
    ["Ash", "Charmander"],
    ["Ash", "Taurus"],
    ["Ash", "Ratata"],
    ["Ash", "Pikachu"],
    ["Ash", "Pidgey"],
    ["Misty", "Starmie"],
    ["Misty", "Togepi"],
    ["Misty", "Staryu"],
    ["Misty", "Horsea"],
    ["Broke", "Nidorina"],
    ["Broke", "Charmander"],
    ["Broke", "Taurus"]
]

pokemon_por_entrenador = defaultdict(list)

for entrenador, pokemon in pokemon_entrenadores_lista:
    pokemon_por_entrenador[entrenador].append(pokemon)    

print("Los pokemon por entrenador son: ", pokemon_por_entrenador)

pokemonListaDiccionario = []

for entrenador, pokemon in pokemon_entrenadores_lista:   
    pokemonDiccionario = {}
    pokemonDiccionario["entrenador"] = entrenador
    pokemonDiccionario["pokemon"] = pokemon
    pokemonListaDiccionario.insert(len(pokemonListaDiccionario), pokemonDiccionario)

print("Lista de Diccionarios :", pokemonListaDiccionario)
 
def letrasComunes(masComunes, frase):
    contador = Counter([letra for letra in frase if letra not in " ,.\n"])   
    return contador.most_common(masComunes)

print("")
print("Frase: ")
frase = "El eterno resplandor de una mente sin recuerdos, las poesías se cumplen y las puertas se abren"
print(frase)
print("")
print("Las 5 letras más comunes son", letrasComunes(9, frase))

def coefJaccard(lista1, lista2):
    union = len(set(lista1).union(set(lista2)))
    interseccion = len(set(lista1).intersection(set(lista2)))    

    return union/interseccion

lista1 = [1, 2, 4, 6, 3, 123, 1]
lista2 = [3, 4, 6, 6]

print("")
print("El coeficiente de Jaccard es: ", coefJaccard(lista1, lista2))