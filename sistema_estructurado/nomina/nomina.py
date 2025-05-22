from nomina.descuentos import Descuentos
from nomina.deducciones import Deducciones
from nomina.beneficios import Beneficios
from nomina.sobretiempo import SobreTiempo

class Nomina:
    def __init__(self, empleado):
        self.empleado = empleado
        self.descuentos = Descuentos()
        self.deducciones = Deducciones()
        self.beneficios = Beneficios()
        self.sobretiempo = SobreTiempo()

    def aplicar_descuentos(self):
        print(f"Aplicando descuentos para {self.empleado.nombre}")
        self.descuentos.faltas = int(input("Faltas: "))
        self.descuentos.tardanzas = int(input("Tardanzas: "))
        total_descuentos = self.descuentos.calcular_descuento()
        print(f"Total descuentos por faltas y tardanzas: {total_descuentos}")


    def aplicar_deducciones(self):
        print("Deducciones legales:")
        self.deducciones.fondo_pension = float(input("Fondo de pensión: "))
        self.deducciones.impuesto_renta = float(input("Impuesto a la renta: "))
        total_deducciones = self.deducciones.calcular_descuentos_ley()
        print(f"Total deducciones legales: {total_deducciones}")

    def aplicar_beneficios(self):
        print("Beneficios:")
        self.beneficios.gratificacion = float(input("Gratificación: "))
        self.beneficios.asignaciones_familiar = float(input("Asignación familiar: "))
        self.beneficios.vacaciones = float(input("Vacaciones: "))
        total_beneficios = self.beneficios.calcular_beneficios()
        print(f"Total beneficios: {total_beneficios}")

    def aplicar_sobretiempo(self):
        print("Horas extra:")
        self.sobretiempo.horas_extra = float(input("Horas extra: "))
        self.sobretiempo.tarifa_sobretiempo = float(input("Tarifa por hora: "))
        pago_extra = self.sobretiempo.calcular_pago_extra()
        print(f"Pago por sobretiempo: {pago_extra}")

    def sueldo_final(self):
        return (
            self.empleado.sueldo_base
            - self.descuentos.calcular_descuento()
            - self.deducciones.calcular_descuentos_ley()
            + self.beneficios.calcular_beneficios()
            + self.sobretiempo.calcular_pago_extra()
        )