class Habitacion:
    def __init__(self, numero, tipo, tarifa):
        self.numero = numero
        self.tipo = tipo
        self.tarifa = tarifa
        self.estado = "Disponible"

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ["Disponible", "Ocupada"]:
            self.estado = nuevo_estado

    def __str__(self):
        return f"Habitación {self.numero} ({self.tipo}) - {self.estado} | Tarifa: ${self.tarifa}"
