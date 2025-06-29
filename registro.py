from modelos import Servicio
from utils import pedir_float, pedir_int, limpiar_pantalla

class GestorServicios:
    def __init__(self):
        self.servicios = []

    def añadir_servicio(self):
        limpiar_pantalla()
        print("\n=== Añadir nuevo servicio ===")
        nombre = input("Nombre del servicio: ").strip()

        materiales = []
        print("Introduce los materiales usados para este servicio:")
        while True:
            mat_nombre = input("Nombre del material (Enter para terminar): ").strip()
            if not mat_nombre:
                break

            coste_total = pedir_float(f"Precio total del producto '{mat_nombre}': ")
            servicio_por_producto = pedir_int(f"¿Cuántos servicios se pueden hacer con '{mat_nombre}'?: ")
            coste_por_servicio = coste_total / servicio_por_producto
            materiales.append((mat_nombre, coste_por_servicio, 1))

        precio_venta = pedir_float("Precio de venta del servicio: ")

        nuevo_servicio = Servicio(nombre, materiales, precio_venta)
        self.servicios.append(nuevo_servicio)
        print(f"Servicio '{nombre}' añadido correctamente.")

    def listar_servicios(self):
        if not self.servicios:
            print("No hay servicios registrados.")
            return
        for idx, servicio in enumerate(self.servicios, 1):
            print(f"\nServicio #{idx}")
            servicio.mostrar_detalles()

    def modificar_servicio(self):
        if not self.servicios:
            print("No hay servicios para modificar.")
            return

        self.listar_servicios()
        idx = pedir_int("\nNúmero del servicio a modificar: ")
        if idx < 1 or idx > len(self.servicios):
            print("Número inválido.")
            return

        servicio = self.servicios[idx - 1]
        limpiar_pantalla()
        print(f"Modificando servicio '{servicio.nombre}'")

        nuevo_nombre = input(f"Nuevo nombre (Enter para mantener '{servicio.nombre}'): ").strip()
        if nuevo_nombre:
            servicio.nombre = nuevo_nombre

        print("Modificando materiales:")
        materiales = []
        while True:
            mat_nombre = input("Nombre del material (Enter para terminar): ").strip()
            if not mat_nombre:
                break
            coste_total = pedir_float(f"Precio total del producto '{mat_nombre}': ")
            servicios_por_producto = pedir_int(f"¿Cuántos servicios se pueden hacer con '{mat_nombre}'?: ")
            coste_por_servicio = coste_total / servicios_por_producto
            materiales.append((mat_nombre, coste_por_servicio, 1))

        if materiales:
            servicio.materiales = materiales

        precio_venta_str = input(f"Nuevo precio de venta (Enter para mantener {servicio.precio_venta}): ").strip()
        if precio_venta_str:
            try:
                servicio.precio_venta = float(precio_venta_str)
            except ValueError:
                print("Precio no válido, se mantiene el anterior.")

        print("Servicio modificado correctamente.")