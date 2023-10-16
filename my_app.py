from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    @abstractmethod
    def calcular_pago(self):
        pass

class Gerente(Empleado):
    def calcular_pago(self):
        return self.salario + 5000

class Desarrollador(Empleado):
    def calcular_pago(self):
        return self.salario + 3000

class Nomina:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def generar_nomina(self):
        if not self.empleados:
            print("No hay empleados en la nómina.")
        else:
            print("\nGenerando Nómina:")
            for empleado in self.empleados:
                print(f"{empleado.nombre}: Salario -> ${empleado.calcular_pago()}")

class Proyecto:
    def __init__(self, nombre, presupuesto):
        self.nombre = nombre
        self.presupuesto = presupuesto

class MenuPrincipal:
    def __init__(self):
        self.nomina = Nomina()
        self.proyectos = []

    def ejecutar(self):
        while True:
            print("\nMenu Principal")
            print("1. Agregar Empleado")
            print("2. Generar Nómina")
            print("3. Agregar Proyecto")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Nombre del empleado: ")
                salario = float(input("Salario del empleado: "))
                tipo_empleado = input("Tipo de empleado (Gerente/Desarrollador): ")
                if tipo_empleado == "Gerente":
                    empleado = Gerente(nombre, salario)
                elif tipo_empleado == "Desarrollador":
                    empleado = Desarrollador(nombre, salario)
                else:
                    print("Tipo de empleado no válido.")
                    continue
                self.nomina.agregar_empleado(empleado)
                print(f"Empleado {nombre} agregado.")

            elif opcion == "2":
                self.nomina.generar_nomina()

            elif opcion == "3":
                nombre_proyecto = input("Nombre del proyecto: ")
                presupuesto = float(input("Presupuesto del proyecto: "))
                proyecto = Proyecto(nombre_proyecto, presupuesto)
                self.proyectos.append(proyecto)
                print(f"Proyecto {nombre_proyecto} agregado.")

            elif opcion == "4":
                break

if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.ejecutar()


