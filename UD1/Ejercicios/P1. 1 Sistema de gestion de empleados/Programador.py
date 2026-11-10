from Empleado import Empleado

class Programador(Empleado):

  def __init__(self, nombre, salario, lenguaje):
    super().__init__(nombre, salario)
    self.lenguaje = lenguaje


  def mostrar_info(self) -> None:
    super().mostrar_info()
    print(f"Lenguaje: {self.lenguaje}")