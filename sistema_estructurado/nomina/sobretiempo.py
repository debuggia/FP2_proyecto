class SobreTiempo:
    def __init__(self, horas_extra=0, tarifa_sobretiempo=0):
        self.horas_extra = horas_extra
        self.tarifa_sobretiempo = tarifa_sobretiempo

    def calcular_pago_extra(self):
        return self.horas_extra * self.tarifa_sobretiempo