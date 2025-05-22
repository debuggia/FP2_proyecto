from .usuario import Usuario
from .empleado import Empleado
from datetime import datetime

class UsuarioObrero(Usuario):
    def __init__(self, username, nombre, apellido, direccion, telefono, fecha_ingreso, cargo, sueldo_base, departamento):
        super().__init__(username, "1234")
        self.empleado = Empleado(nombre, direccion, telefono,
                                 fecha_ingreso.strftime("%Y-%m-%d") if isinstance(fecha_ingreso, datetime) else fecha_ingreso,
                                 cargo, departamento, sueldo_base)

class UsuarioRecursosHumanos(Usuario):
    def __init__(self, username, nombre, apellido, direccion, telefono, fecha_ingreso):
        super().__init__(username, "1234")
        self.nombre = nombre
        self.apellido = apellido