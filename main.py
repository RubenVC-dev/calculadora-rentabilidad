from registro import añadir_servicio, ver_servicios
from calculo import calcular_beneficio_mensual

def menu():
    print("\n=== ANÁLISIS DE RENTABILIDAD MENSUAL ===")
    while True:
        print("\n--- Menú Principal ---")
        print("1. Añadir un servicio")
        print("2. Ver servicios registrados")
        print("3. Calcular beneficios mensuales")
        print("4. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            añadir_servicio()
        elif opcion == "2":
            ver_servicios()
        elif opcion == "3":
            calcular_beneficio_mensual()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()