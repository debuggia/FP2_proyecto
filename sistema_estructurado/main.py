from datetime import datetime
from sistema import SistemaEmpleados
from usuarios.roles import UsuarioObrero, UsuarioRecursosHumanos
from nomina.nomina import Nomina

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


def iniciar_sesion():
    username = input("Usuario: ")
    password = input("Contraseña: ")
    if username in obreros and obreros[username].password == password:
        return obreros[username]
    elif username in recursos_humanos and recursos_humanos[username].password == password:
        return recursos_humanos[username]
    else:
        print("Credenciales incorrectas.")
        return None

def main():
    sistema = SistemaEmpleados()
    for obrero in obreros.values():
        sistema.agregar_empleado(obrero.empleado)

    usuario = iniciar_sesion()
    if not usuario:
        return

    if isinstance(usuario, UsuarioObrero):
        emp = usuario.empleado
        emp.registrar_asistencia("2025-05-18", "08:00", "ingreso")
        emp.registrar_asistencia("2025-05-18", "17:00", "salida")
        for k, v in emp.ver_datos().items():
            print(f"{k}: {v}")

    elif isinstance(usuario, UsuarioRecursosHumanos):
        while True:
            sistema.mostrar_empleados()
            try:
                codigo = int(input("Código de empleado: "))
                emp = sistema.obtener_empleado_por_codigo(codigo)
                if not emp:
                    print("Empleado no encontrado.")
                    continue
                nomina = Nomina(emp)
                while True:
                    print("\n1. Descuentos\n2. Deducciones\n3. Beneficios\n4. Sobretiempo\n5. Sueldo Final\n6. Otro empleado\n7. Salir")
                    opcion = input("Opción: ")
                    if opcion == "1": nomina.aplicar_descuentos()
                    elif opcion == "2": nomina.aplicar_deducciones()
                    elif opcion == "3": nomina.aplicar_beneficios()
                    elif opcion == "4": nomina.aplicar_sobretiempo()
                    elif opcion == "5": print(f"Sueldo Final: {nomina.sueldo_final()}")
                    elif opcion == "6": break
                    elif opcion == "7": return
            except ValueError:
                print("Código inválido.")

if __name__ == "__main__":
    main()