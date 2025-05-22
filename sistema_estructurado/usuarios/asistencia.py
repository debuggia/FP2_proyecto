class Asistencia:
    def __init__(self, fecha):
        self.fecha = fecha
        self.hora_ingreso = None
        self.hora_salida = None

    def registrar_ingreso(self, hora):
        self.hora_ingreso = hora
        print(f"[INFO] Ingreso registrado a las {hora}.")

    def registrar_salida(self, hora):
        self.hora_salida = hora
        print(f"[INFO] Salida registrada a las {hora}.")

    def __str__(self):
        return f"Fecha: {self.fecha} | Ingreso: {self.hora_ingreso or 'N/A'} | Salida: {self.hora_salida or 'N/A'}"