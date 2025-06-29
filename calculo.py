from datos import servicios

def calcular_beneficio_mensual():
    if not servicios:
        print("\nPrimero debes registrar al menos un servicio.")
        return

    print("\n--- Frecuencia de servicios ---")
    try:
        dias_trabajo = int(input("¿Cuántos días trabajas al mes?: "))
    except ValueError:
        print("Número inválido de días.")
        return

    beneficio_total = 0
    usos_servicios = {}

    for servicio in servicios:
        try:
            por_dia = int(input(f"¿Cuántas veces haces '{servicio['nombre']}' al día?: "))
        except ValueError:
            print("Número inválido. Se asumirá 0.")
            por_dia = 0
        veces = por_dia * dias_trabajo
        usos_servicios[servicio['nombre']] = veces
        ganancia_unidad = servicio['precio'] - servicio['costo_materiales']
        beneficio_servicio = ganancia_unidad * veces
        beneficio_total += beneficio_servicio

    try:
        gastos_fijos = float(input("\nGastos fijos mensuales: € "))
        sueldo_deseado = float(input("Sueldo deseado al mes: € "))
    except ValueError:
        print("Entrada inválida.")
        return

    total_necesario = gastos_fijos + sueldo_deseado
    diferencia = beneficio_total - total_necesario

    print("\n--- RESULTADO ---")
    print(f"Beneficio mensual estimado: {beneficio_total:.2f} €")
    print(f"Necesario para cubrir todo: {total_necesario:.2f} €")

    if diferencia >= 0:
        print(f"Estás generando un excedente de {diferencia:.2f} € al mes.")
    else:
        falta = -diferencia
        subida = falta / sum(usos_servicios.values())
        print(f"Faltan {falta:.2f} € para alcanzar el objetivo.")
        print(f"Deberías subir cada servicio una media de {subida:.2f} €")

    guardar = input("\n¿Deseas guardar este informe? (s/n): ").lower()
    if guardar == "s":
        with open("analisis_completo.txt", "w", encoding="utf-8") as archivo:
            archivo.write("--- ANÁLISIS DE RENTABILIDAD ---\n")
            for servicio in servicios:
                archivo.write(f"\nServicio: {servicio['nombre']}\n")
                archivo.write(f"Precio venta: {servicio['precio']:.2f} €\n")
                archivo.write(f"Coste materiales: {servicio['costo_materiales']:.2f} €\n")
                archivo.write(f"Veces al mes: {usos_servicios.get(servicio['nombre'], 0)}\n")
                archivo.write("Materiales usados:\n")
                for mat in servicio['materiales']:
                    archivo.write(f"  - {mat[0]}: {mat[1]:.2f} € por {mat[2]} usos → {mat[3]:.2f} € por servicio\n")
            archivo.write(f"\nBeneficio mensual total: {beneficio_total:.2f} €\n")
            archivo.write(f"Total necesario: {total_necesario:.2f} €\n")
            if diferencia >= 0:
                archivo.write(f"Excedente: {diferencia:.2f} €\n")
            else:
                archivo.write(f"Déficit: {falta:.2f} €\n")
                archivo.write(f"Subida media sugerida: {subida:.2f} €\n")
        print("\nInforme guardado en 'analisis_completo.txt'")