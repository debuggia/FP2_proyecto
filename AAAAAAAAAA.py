from datetime import datetime

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
    _codigo_counter = 1  # variable para asignar código único a cada empleado

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
        nueva_asistencia = Asistencia(fecha)
        self.asistencias.append(nueva_asistencia)
        return nueva_asistencia


class Descuentos:
    def __init__(self, faltas=0, tardanzas=0):
        self.faltas = faltas
        self.tardanzas = tardanzas

    def calcular_descuento(self):
        # Supongamos que cada falta descuenta 100 y cada tardanza 50
        return (self.faltas * 100) + (self.tardanzas * 50)


class Deducciones:
    def __init__(self, fondo_pension=0, impuesto_renta=0):
        self.fondo_pension = fondo_pension
        self.impuesto_renta = impuesto_renta

    def calcular_descuentos_ley(self):
        # Suma total de deducciones legales
        return self.fondo_pension + self.impuesto_renta


class Beneficios:
    def __init__(self, gratificacion=0, asignaciones_familiar=0, vacaciones=0):
        self.gratificacion = gratificacion
        self.asignaciones_familiar = asignaciones_familiar
        self.vacaciones = vacaciones

    def calcular_beneficios(self):
        return self.gratificacion + self.asignaciones_familiar + self.vacaciones


class SobreTiempo:
    def __init__(self, horas_extra=0, tarifa_sobretiempo=0):
        self.horas_extra = horas_extra
        self.tarifa_sobretiempo = tarifa_sobretiempo

    def calcular_pago_extra(self):
        return self.horas_extra * self.tarifa_sobretiempo


class Nomina:
    def __init__(self, empleado):
        self.empleado = empleado
        self.descuentos = Descuentos()
        self.deducciones = Deducciones()
        self.beneficios = Beneficios()
        self.sobretiempo = SobreTiempo()

    def aplicar_descuentos(self):
        print(f"Aplicando descuentos para empleado {self.empleado.codigo} - {self.empleado.nombre}")
        self.descuentos.faltas = int(input("Ingrese el número de faltas: "))
        self.descuentos.tardanzas = int(input("Ingrese el número de tardanzas: "))
        total_descuentos = self.descuentos.calcular_descuento()
        print(f"Total descuentos por faltas y tardanzas: {total_descuentos}")

    def aplicar_deducciones(self):
        print("Ahora, ingrese las deducciones legales (fondo de pensión e impuesto a la renta).")
        self.deducciones.fondo_pension = float(input("Ingrese monto de fondo de pensión: "))
        self.deducciones.impuesto_renta = float(input("Ingrese monto de impuesto a la renta: "))
        total_deducciones = self.deducciones.calcular_descuentos_ley()
        print(f"Total deducciones legales: {total_deducciones}")

    def aplicar_beneficios(self):
        print("Ahora, ingrese los beneficios para el empleado.")
        self.beneficios.gratificacion = float(input("Ingrese la gratificación: "))
        self.beneficios.asignaciones_familiar = float(input("Ingrese las asignaciones familiares: "))
        self.beneficios.vacaciones = float(input("Ingrese el monto de vacaciones: "))
        total_beneficios = self.beneficios.calcular_beneficios()
        print(f"Total beneficios: {total_beneficios}")

    def aplicar_sobretiempo(self):
        print("Ingrese información de horas extra para sobretiempo.")
        self.sobretiempo.horas_extra = float(input("Ingrese el número de horas extra: "))
        self.sobretiempo.tarifa_sobretiempo = float(input("Ingrese la tarifa por hora extra: "))
        pago_extra = self.sobretiempo.calcular_pago_extra()
        print(f"Pago por sobretiempo: {pago_extra}")

    def sueldo_final(self):
        total_descuentos = self.descuentos.calcular_descuento() + self.deducciones.calcular_descuentos_ley()
        total_beneficios = self.beneficios.calcular_beneficios()
        total_sobretiempo = self.sobretiempo.calcular_pago_extra()
        sueldo_final = self.empleado.sueldo_base - total_descuentos + total_beneficios + total_sobretiempo
        return sueldo_final

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UsuarioObrero(Usuario):
    def __init__(self, username, nombre, apellido, direccion, telefono, fecha_ingreso, cargo, sueldo_base, departamento):
        super().__init__(username, "1234")  # Contraseña fija 1234
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_ingreso = fecha_ingreso
        self.cargo = cargo
        self.sueldo_base = sueldo_base
        self.departamento = departamento
        # Crear instancia interna de Empleado para manejar asistencias y datos
        self.empleado = Empleado(nombre, direccion, telefono,
                                 fecha_ingreso.strftime("%Y-%m-%d") if isinstance(fecha_ingreso, datetime) else fecha_ingreso,
                                 cargo, departamento, sueldo_base)

class UsuarioRecursosHumanos(Usuario):
    def __init__(self, username, nombre, apellido, direccion, telefono, fecha_ingreso):
        super().__init__(username, "1234")  # Contraseña fija 1234
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.fecha_ingreso = fecha_ingreso

# Instancias de usuarios con contraseña 1234 fija
obreros = {
    "obrero1": UsuarioObrero("obrero1", "Juan", "Perez", "Av. Principal 123", "987654321", datetime(2020, 1, 15), "Operario", 1000, "Producción"),
    "obrero2": UsuarioObrero("obrero2", "Maria", "Lopez", "Calle Secundaria 456", "987654322", datetime(2021, 2, 20), "Auxiliar", 900, "Mantenimiento"),
    "obrero3": UsuarioObrero("obrero3", "Carlos", "Gonzalez", "Av. Central 789", "987654323", datetime(2022, 3, 25), "Técnico", 1100, "Calidad"),
    "obrero4": UsuarioObrero("obrero4", "Ana", "Martinez", "Calle Tercera 101", "987654324", datetime(2021, 4, 30), "Supervisor", 1200, "Producción"),
    "obrero5": UsuarioObrero("obrero5", "Luis", "Fernandez", "Av. Cuarta 202", "987654325", datetime(2020, 5, 5), "Operario", 950, "Logística"),
}

recursos_humanos = {
    "rh1": UsuarioRecursosHumanos("rh1", "Ana", "Gomez", "Calle Recursos 1", "987654326", datetime(2019, 6, 10)),
    "rh2": UsuarioRecursosHumanos("rh2", "Luis", "Martinez", "Calle Recursos 2", "987654327", datetime(2018, 7, 15)),
    "rh3": UsuarioRecursosHumanos("rh3", "Pedro", "Sanchez", "Calle Recursos 3", "987654328", datetime(2020, 8, 20)),
    "rh4": UsuarioRecursosHumanos("rh4", "Laura", "Torres", "Calle Recursos 4", "987654329", datetime(2021, 9, 25)),
    "rh5": UsuarioRecursosHumanos("rh5", "Javier", "Ramirez", "Calle Recursos 5", "987654330", datetime(2022, 10, 30)),
}

class SistemaEmpleados:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        print("\nLista de Empleados:")
        for emp in self.empleados:
            print(f"Código: {emp.codigo} | Nombre: {emp.nombre} | Sueldo base: {emp.sueldo_base}")

    def obtener_empleado_por_codigo(self, codigo):
        for emp in self.empleados:
            if emp.codigo == codigo:
                return emp
        return None

def iniciar_sesion():
    print("Iniciar Sesión")
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    if username in obreros and obreros[username].password == password:
        return obreros[username]
    elif username in recursos_humanos and recursos_humanos[username].password == password:
        return recursos_humanos[username]
    else:
        print("Credenciales incorrectas.")
        return None

def main():
    sistema = SistemaEmpleados()

    # Agregar todos los empleados obreros a sistema.empleados para gestión nómina
    for obrero in obreros.values():
        sistema.agregar_empleado(obrero.empleado)

    # Iniciar sesión
    usuario = iniciar_sesion()
    if not usuario:
        return

    if isinstance(usuario, UsuarioObrero):
        emp = usuario.empleado
        # Ejemplo: registrar asistencia para mostrar
        emp.registrar_asistencia("2025-05-18", "08:00", "ingreso")
        emp.registrar_asistencia("2025-05-18", "17:00", "salida")

        datos = emp.ver_datos()
        print("\n[DATOS DEL EMPLEADO]")
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")

        print("\n[ASISTENCIAS]")
        for asistencia in emp.asistencias:
            print(asistencia)

    elif isinstance(usuario, UsuarioRecursosHumanos):
        print(f"\nBienvenido, {usuario.nombre} {usuario.apellido}. Accediendo al sistema de Nómina.")
        while True:
            sistema.mostrar_empleados()
            try:
                cod = int(input("\nIngrese el código del empleado para gestionar su nómina: "))
            except ValueError:
                print("Código inválido.")
                continue

            empleado_seleccionado = sistema.obtener_empleado_por_codigo(cod)
            if not empleado_seleccionado:
                print("Empleado no encontrado.")
                continue

            print(f"\nEmpleado seleccionado: {empleado_seleccionado.nombre} - Sueldo Base: {empleado_seleccionado.sueldo_base}")
            nomina = Nomina(empleado_seleccionado)

            while True:
                print("\nOpciones:")
                print("1. Aplicar descuentos")
                print("2. Aplicar deducciones")
                print("3. Aplicar beneficios")
                print("4. Aplicar sobretiempo")
                print("5. Mostrar resumen de sueldo final")
                print("6. Elegir otro empleado")
                print("7. Salir")

                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    nomina.aplicar_descuentos()
                elif opcion == "2":
                    nomina.aplicar_deducciones()
                elif opcion == "3":
                    nomina.aplicar_beneficios()
                elif opcion == "4":
                    nomina.aplicar_sobretiempo()
                elif opcion == "5":
                    print("\n[RESUMEN DE NÓMINA]")
                    print(f"Empleado: {empleado_seleccionado.nombre}")
                    print(f"Sueldo Base: {empleado_seleccionado.sueldo_base}")
                    print(f"Sueldo Final: {nomina.sueldo_final()}")
                elif opcion == "6":
                    break  # volver a elegir otro empleado
                elif opcion == "7":
                    print("Saliendo...")
                    return
                else:
                    print("Opción inválida, por favor intente nuevamente.")
    else:
        print("Tipo de usuario no reconocido.")

if __name__ == "__main__":
    main()

