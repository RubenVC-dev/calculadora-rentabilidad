class Servicio:
    def __init__(self, nombre: str, materiales: list[tuple[str, float, float]], precio_venta: float):
        """
        Inicializa un nuevo servicio.

        Parámetros:
        - nombre (str): nombre del servicio.
        - materiales (list): lista de tuplas con los materiales usados,
                             cada tupla tiene: (nombre_material, coste_por_servicio, unidades_usadas).
        - precio_venta (float): precio al que se vende el servicio.
        """
        self.nombre = nombre
        self.materiales = materiales
        self.precio_venta = precio_venta

    def calcular_coste_materiales(self) -> float:
        """Calcula el coste total de materiales para este servicio."""
        coste_total = 0
        for nombre, coste_unitario, unidades in self.materiales:
            coste_total += coste_unitario * unidades
        return coste_total

    def calcular_beneficio(self) -> float:
        """Calcula el beneficio neto del servicio (precio de venta - coste de materiales)."""
        return self.precio_venta - self.calcular_coste_materiales()

    def es_rentable(self) -> bool:
        """Devuelve True si el beneficio es mayor que 0."""
        return self.calcular_beneficio() > 0

    def precio_minimo(self) -> float:
        """Devuelve el precio mínimo necesario para no perder dinero."""
        return self.calcular_coste_materiales()

    def precio_recomendado(self) -> float:
        """Calcula el precio de venta recomendado para obtener un 30% de beneficio."""
        return round(self.precio_minimo() * 1.3, 2)

    def obtener_resumen(self) -> str:
        """Devuelve un string con todos los detalles del servicio."""
        detalles = [
            f"Servicio: {self.nombre}",
            f"Precio de venta: {self.precio_venta:.2f} €",
            "Materiales usados:"
        ]
        for nombre, coste_unitario, unidades in self.materiales:
            detalles.append(f" - {nombre}: {unidades} unidad(es) x {coste_unitario:.2f} €")
        detalles.append(f"Coste total en materiales: {self.calcular_coste_materiales():.2f} €")
        detalles.append(f"Beneficio: {self.calcular_beneficio():.2f} €")
        detalles.append("Rentable" if self.es_rentable() else "No rentable")
        detalles.append(f"Precio mínimo para no perder: {self.precio_minimo():.2f} €")
        detalles.append(f"Precio recomendado (30% beneficio): {self.precio_recomendado():.2f} €")

        return "\n".join(detalles)

    def mostrar_detalles(self) -> None:
        """Imprime los detalles del servicio en pantalla."""
        print(self.obtener_resumen())