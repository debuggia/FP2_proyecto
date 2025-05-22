class SistemaEmpleados:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        print("\nEmpleados:")
        for emp in self.empleados:
            print(f"{emp.codigo}: {emp.nombre} | Sueldo: {emp.sueldo_base}")

    def obtener_empleado_por_codigo(self, codigo):
        return next((emp for emp in self.empleados if emp.codigo == codigo), None)