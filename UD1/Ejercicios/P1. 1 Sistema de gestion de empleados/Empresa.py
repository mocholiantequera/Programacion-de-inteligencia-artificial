from Empleado import Empleado


class Empresa:
  def __init__(self):
    self._empleados: dict[str, Empleado] = {}

  def añadir(self, empleado: Empleado) -> bool:
    clave = empleado.nombre.lower()
    if clave in self._empleados:
      return False

    self._empleados[clave] = empleado
    return True

  def buscar(self, nombre: str):
    for e in self._empleados.values():
      if e.nombre.lower() == nombre.lower():
        return e
    return None

  def listar(self):
    copia = list(self._empleados.values())
    copia.sort(key=lambda e: e.salario, reverse=True)
    return copia


  def gastoTotal(self) -> float:
    total = 0
    for e in self._empleados.values():
      total += e.salario
    return total