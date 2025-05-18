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


class Empleado:
    def __init__(self, nombre, direccion, telefono, fecha_ingreso, cargo, departamento, sueldo_base):
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
        nueva_asistencia = Asistencia(fecha)
        self.asistencias.append(nueva_asistencia)
        return nueva_asistencia
    
    # Crear un empleado
empleado = Empleado(
    nombre="Juan Pérez",
    direccion="Calle 123",
    telefono="555-1234",
    fecha_ingreso="2023-01-10",
    cargo="Analista",
    departamento="TI",
    sueldo_base=5000
)

# Registrar ingreso el 2025-05-18 a las 08:00
empleado.registrar_asistencia("2025-05-18", "08:00", "ingreso")

# Registrar salida el 2025-05-18 a las 17:00
empleado.registrar_asistencia("2025-05-18", "17:00", "salida")

# Ver datos del empleado
datos = empleado.ver_datos()
print("\n[DATOS DEL EMPLEADO]")
for clave, valor in datos.items():
    print(f"{clave}: {valor}")

# Ver detalles de asistencias
print("\n[ASISTENCIAS]")
for asistencia in empleado.asistencias:
    print(asistencia)

