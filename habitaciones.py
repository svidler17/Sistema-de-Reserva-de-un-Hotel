#clase de la habitacion
# Clase Habitación
class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.estado = "Disponible"
        self.fecha_ingreso = None
        self.fecha_salida = None
        self.metodo_pago = None
        self.total = 0

    def calcular_total(self, precio_por_dia):
        """Calcula el total con base en los días de estancia"""
        if self.fecha_ingreso and self.fecha_salida:
            dias = (self.fecha_salida - self.fecha_ingreso).days
            if dias <= 0:
                dias = 1
            self.total = dias * precio_por_dia
            return self.total
        return 0

    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado de la habitación"""
        if nuevo_estado not in ["Disponible", "Ocupada", "Mantenimiento"]:
            print("Estado no válido.")
        else:
            self.estado = nuevo_estado
            print(f"Estado actualizado a: {self.estado}")

    def __str__(self):
        if self.estado == "Ocupada" and self.fecha_ingreso and self.fecha_salida:
            return (f"Habitación {self.numero} ({self.tipo}) - {self.estado} | "
                    f"Desde: {self.fecha_ingreso.date()} Hasta: {self.fecha_salida.date()} | "
                    f"Método de pago: {self.metodo_pago} | Total: ${self.total}")
        else:
            return f"Habitación {self.numero} ({self.tipo}) - {self.estado}"


# Clase Hotel solo para habitaciones)
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        # Evitar que se repitan números de habitación
        if any(h.numero == habitacion.numero for h in self.habitaciones):
            print("Ya existe una habitación con ese número.")
            return
        self.habitaciones.append(habitacion)
        print(f"Habitación registrada: {habitacion}")

    def mostrar_habitaciones(self):
        if not self.habitaciones:
            print("\nNo hay habitaciones registradas.")
            return
        print("\n--- Habitaciones ---")
        for hab in self.habitaciones:
            print(hab)
       
