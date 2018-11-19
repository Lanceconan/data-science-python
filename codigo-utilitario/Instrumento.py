class Instrumento:

    def __init__(
        self, largo = 0, 
        ancho = 0, 
        alto = 0, 
        decibeles = 0, 
        estaSonando =False
    ):
        self.largo = largo
        self.ancho = ancho 
        self.alto = alto
        self.decibeles = decibeles
        self.estaSonando = estaSonando

    def tocar(self, pieza):
        print('comenzó a sonar pieza', pieza)
        self.estaSonando = True

    def parar(self, pieza):
        print('Paró de tocar pieza', pieza)
        self.estaSonando = False