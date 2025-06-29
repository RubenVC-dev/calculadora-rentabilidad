from datos import servicios

def añadir_servicio():
    nombre_servicio = input("\nNombre del servicio: ").strip()
    try:
        precio_venta = float(input(f"Precio del servicio '{nombre_servicio}': € "))
        materiales = []

        print(f"Introduce los materiales usados en '{nombre_servicio}':")
        while True:
            nombre_mat = input("  - Nombre del material (o Enter para terminar): ").strip()
            if nombre_mat == "":
                break
            precio_total = float(input(f"    Precio del producto '{nombre_mat}': € "))
            usos = int(input(f"    ¿Cuántos servicios puedes hacer con '{nombre_mat}'?: "))
            costo_unitario = precio_total / usos
            materiales.append((nombre_mat, precio_total, usos, costo_unitario))

        costo_materiales = sum(m[3] for m in materiales)

        servicios.append({
            "nombre": nombre_servicio,
            "precio": precio_venta,
            "materiales": materiales,
            "costo_materiales": costo_materiales
        })

        print(f"Servicio '{nombre_servicio}' añadido correctamente.")

    except ValueError:
        print("Entrada no válida. Intenta de nuevo.")

def ver_servicios():
    if not servicios:
        print("\nNo hay servicios registrados todavía.")
    else:
        print("\n--- Servicios Registrados ---")
        for s in servicios:
            print(f"- {s['nombre']} | Precio: {s['precio']} € | Coste materiales: {s['costo_materiales']:.2f} €")