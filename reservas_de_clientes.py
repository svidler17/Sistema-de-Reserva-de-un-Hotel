class Reserva:
    def __init__(self, id_reserva, cliente, habitacion, dias_estadia):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias_estadia = dias_estadia
        self.estado = "Activa"

    def modificar_reserva(self, nuevos_dias):
        if self.estado != "Activa":
            print("No se puede modificar una reserva que no está activa.")
            return
        if nuevos_dias <= 0:
            print("La cantidad de días debe ser mayor a cero.")
            return
        self.dias_estadia = nuevos_dias
        self.habitacion.dias_estadia = nuevos_dias
        print(f"Reserva modificada correctamente. Nueva estancia: {nuevos_dias} días.")

    def cancelar_reserva(self):
        if self.estado == "Cancelada":
            print("La reserva ya estaba cancelada.")
        else:
            self.estado = "Cancelada"
            self.habitacion.cambiar_estado("Disponible")
            self.habitacion.dias_estadia = 0
            print(f"Reserva {self.id_reserva} cancelada correctamente y habitación liberada.")

    def mostrar_resumen(self):
        print(f"\n--- Detalles de la Reserva ---")
        print(f"ID Reserva: {self.id_reserva}")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Habitación: {self.habitacion.numero} ({self.habitacion.tipo})")
        print(f"Días de estancia: {self.dias_estadia}")
        print(f"Estado: {self.estado}")
        print(f"Total estimado: ${self.habitacion.tarifa * self.dias_estadia:.2f}")

    def __str__(self):
        return (f"Reserva {self.id_reserva}: {self.cliente.nombre} - "
                f"Habitación {self.habitacion.numero} ({self.dias_estadia} días) - Estado: {self.estado}")
