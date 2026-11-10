from Empleado import Empleado

class Diseñador(Empleado):

  def __init__(self, nombre, salario, herramienta):
    super().__init__(nombre, salario)
    self.herramienta = herramienta


  def mostrar_info(self) -> None:
    super().mostrar_info()
    print(f"Herramienta: {self.herramienta}")