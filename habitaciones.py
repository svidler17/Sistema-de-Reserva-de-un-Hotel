class Habitacion:
    def _init_(self, numero, tipo, tarifa):
        self.numero = numero
        self.tipo = tipo
        self.tarifa = tarifa
        self.estado = "Disponible"

    def cambiar_estado(self, nuevo_estado):
        estados_validos = ["Disponible", "Ocupada", "Mantenimiento"]
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
        else:
            print("Estado no válido. Intente de nuevo.")

    def _str_(self):
        return f"Habitación {self.numero} ({self.tipo}) - {self.estado} | Tarifa: ${self.tarifa}"
