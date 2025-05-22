class Deducciones:
    def __init__(self, fondo_pension=0, impuesto_renta=0):
        self.fondo_pension = fondo_pension
        self.impuesto_renta = impuesto_renta

    def calcular_descuentos_ley(self):
        return self.fondo_pension + self.impuesto_renta