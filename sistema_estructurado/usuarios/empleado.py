from .asistencia import Asistencia

class Empleado:
    _codigo_counter = 1

    def __init__(self, nombre, direccion, telefono, fecha_ingreso, cargo, departamento, sueldo_base):
        self.codigo = Empleado._codigo_counter
        Empleado._codigo_counter += 1
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_ingreso = fecha_ingreso
        self.cargo = cargo
        self.departamento = departamento
        self.sueldo_base = sueldo_base
        self.asistencias = []

    def ver_datos(self):
        return {
            "Nombre": self.nombre,
            "Dirección": self.direccion,
            "Teléfono": self.telefono,
            "Fecha de ingreso": self.fecha_ingreso,
            "Cargo": self.cargo,
            "Departamento": self.departamento,
            "Sueldo base": self.sueldo_base,
            "Asistencias": [str(a) for a in self.asistencias]
        }

    def registrar_asistencia(self, fecha, hora, tipo):
        asistencia = self._obtener_o_crear_asistencia(fecha)
        if tipo == "ingreso":
            asistencia.registrar_ingreso(hora)
        elif tipo == "salida":
            asistencia.registrar_salida(hora)

    def _obtener_o_crear_asistencia(self, fecha):
        for a in self.asistencias:
            if a.fecha == fecha:
                return a
        nueva = Asistencia(fecha)
        self.asistencias.append(nueva)
        return nueva