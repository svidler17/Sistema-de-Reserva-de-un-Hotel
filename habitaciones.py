# =========================================================
#  Clase Habitación
# =========================================================
class Habitacion:
    def __init__(self, numero, tipo, tarifa):
        self.numero = numero
        self.tipo = tipo
        self.tarifa = tarifa
        self.estado = "Disponible"
        self.dias_estadia = 0
        self.metodo_pago = None
        self.total = 0

    def calcular_total(self):
        if self.dias_estadia <= 0:
            self.dias_estadia = 1
        self.total = self.dias_estadia * self.tarifa
        return self.total

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado not in ["Disponible", "Ocupada", "Mantenimiento"]:
            print("Estado no válido.")
        else:
            self.estado = nuevo_estado
            print(f"Estado actualizado a: {self.estado}")

    def __str__(self):
        return (f"Habitación {self.numero} ({self.tipo}) - {self.estado} | "
                f"Días: {self.dias_estadia} | Total: ${self.total}")
