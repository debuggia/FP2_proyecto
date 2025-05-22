class Beneficios:
    def __init__(self, gratificacion=0, asignaciones_familiar=0, vacaciones=0):
        self.gratificacion = gratificacion
        self.asignaciones_familiar = asignaciones_familiar
        self.vacaciones = vacaciones

    def calcular_beneficios(self):
        return self.gratificacion + self.asignaciones_familiar + self.vacaciones