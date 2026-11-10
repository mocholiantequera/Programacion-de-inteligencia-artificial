class Empleado:


  def __init__(self, nombre, salario ):
    self.nombre = nombre
    self.salario = salario

  def subir_salario(self, porcentaje: float) -> None:
    if porcentaje <=0:
      print ("Error el porcentaje tiene que ser mayor de 0")
    else:
      self.salario = self.salario + (self.salario * porcentaje / 100)
      print ("Salario modificado correctamente")

  def mostrar_info(self) -> None:
    print (f"Nombre del empleado: {self.nombre}")
    print (f"salario del empleado: {self.salario}")