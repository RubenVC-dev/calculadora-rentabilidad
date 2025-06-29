from registro import GestorServicios
from utils import limpiar_pantalla

class Aplicacion:
    def __init__(self):
        self.gestor = GestorServicios()

    def menu(self):
        while True:
            limpiar_pantalla()
            print("\n=== ANÁLISIS DE RENTABILIDAD MENSUAL ===")
            print("1. Añadir un servicio")
            print("2. Ver servicios registrados")
            print("3. Modificar un servicio")
            print("4. Calcular beneficio mensual total")
            print("5. Salir")

            opcion = input("Selecciona una opción: ").strip()
            limpiar_pantalla()

            if opcion == "1":
                self.gestor.añadir_servicio()
            elif opcion == "2":
                self.gestor.listar_servicios()
                input("\nPulsa Enter para volver al menú...")
            elif opcion == "3":
                self.gestor.modificar_servicio()
                input("\nPulsa Enter para volver al menú...")
            elif opcion == "4":
                self.calcular_beneficio_mensual()
                input("\nPulsa Enter para volver al menú...")
            elif opcion == "5":
                print("Saliendo del programa. ¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
                input("\nPulsa Enter para volver al menú...")

    def calcular_beneficio_mensual(self):
        if not self.gestor.servicios:
            print("No hay servicios registrados para calcular beneficios.")
            return

        print("\n=== Beneficios de cada servicio ===")
        beneficio_total = 0
        for servicio in self.gestor.servicios:
            beneficio = servicio.calcular_beneficio()
            print(f"- {servicio.nombre}: {beneficio:.2f} €")
            beneficio_total += beneficio

        print(f"\nBeneficio mensual total: {beneficio_total:.2f} €")

if __name__ == "__main__":
    app = Aplicacion()
    app.menu()