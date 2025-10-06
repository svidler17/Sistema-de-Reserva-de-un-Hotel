#clase de la habitacion
class Habitaciones:
  def __init__(self, numero, tipo):
    self.numero = numero
    self.tipo = tipo
    self.estado = "DISPONIBLE"

  def __str__(self):
    return f"Habitacion {self.numero} ({self.tipo}) - {self.estado}"
