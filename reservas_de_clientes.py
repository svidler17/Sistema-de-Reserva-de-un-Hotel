class Reserva:
    def __init__(self, id_reserva, cliente, habitacion, dias_estadia):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias_estadia = dias_estadia
        self.estado = "Activa"
        self.total = habitacion.tarifa * dias_estadia
        self.pagado = 0.0

    def cancelar(self):
        self.estado = "Cancelada"
        self.habitacion.cambiar_estado("Disponible")

    def registrar_pago(self, monto):
        self.pagado += monto
        return self.pagado

    def saldo_pendiente(self):
        return self.total - self.pagado

    def __str__(self):
        total = int(self.total) if self.total.is_integer() else self.total
        pagado = int(self.pagado) if self.pagado.is_integer() else self.pagado
        return (f"Reserva {self.id_reserva}: {self.cliente.nombre} - "
                f"Habitación {self.habitacion.numero} ({self.habitacion.tipo}) - "
                f"{self.dias_estadia} días - Estado: {self.estado} - Total: ${total} - Pagado: ${pagado}")
