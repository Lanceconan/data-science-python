import math

class Newton:
    def __init__(
        self,         
        velocidadInicial,
        velocidadFinal,
        altura,
        tiempo, 
        masa,
        g = 9.8
    ):
        self.masa = masa
        self.tiempo = tiempo
        self.altura = altura
        self.velocidadInicial = velocidadInicial
        self.velocidadFinal = velocidadFinal
        self.g = g        

    #METODOS
    
    def distancia(self):
        return (self.velocidadInicial * self.tiempo) + math.pow(self.tiempo, 2) * 0.5 * self.aceleracion()

    def aceleracion(self):
        return float(self.velocidadFinal - self.velocidadInicial) / self.tiempo

    def fuerza(self):
        return self.masa * self.aceleracion()

    def energiaPotencial(self):
        return (0.5 * self.masa * math.pow(self.velocidadFinal,2))

    def energiaCinetica(self):
        return (self.altura * self.masa * self.g)

    

    