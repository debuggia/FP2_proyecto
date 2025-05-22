class Descuentos:
    def __init__(self, faltas=0, tardanzas=0):
        self.faltas = faltas
        self.tardanzas = tardanzas

    def calcular_descuento(self):
        return self.faltas * 100 + self.tardanzas * 50