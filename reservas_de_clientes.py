class Cliente:
    def __init__(self, id_cliente, nombre):
        self.id_cliente = id_cliente
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_cliente})"

class Habitacion:
    def __init__(self, numero, tipo, tarifa):
        self.numero = numero
        self.tipo = tipo
        self.tarifa = tarifa
        self.estado = "disponible"  # disponible, ocupada, mantenimiento

    def __str__(self):
        return f"Habitación {self.numero} ({self.tipo}) - {self.estado}"

class Reserva:
    def __init__(self, id_reserva, cliente, habitacion, fecha_inicio, fecha_fin):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = "activa"  # activa, cancelada, finalizada

def modificar_reserva(self, nueva_fecha_inicio, nueva_fecha_fin):
        if self.estado != "activa":
            print(" No se puede modificar una reserva que no está activa.")
            return
        self.fecha_inicio = nueva_fecha_inicio
        self.fecha_fin = nueva_fecha_fin
        print("Reserva modificada correctamente.")

    def cancelar_reserva(self):
        if self.estado == "cancelada":
            print(" La reserva ya estaba cancelada.")
        else:
            self.estado = "cancelada"
            self.habitacion.estado = "disponible"
            print("Reserva cancelada correctamente.")

    def __str__(self):
        return (f"Reserva {self.id_reserva}: {self.cliente.nombre} - Habitación {self.habitacion.numero} "
                f"({self.fecha_inicio.date()} → {self.fecha_fin.date()}) - Estado: {self.estado}")
