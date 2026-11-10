from Empresa import Empresa
from Diseñador import Diseñador
from Programador import Programador

empresa = Empresa()
while True:
  print ("\n === Sistema de Gestión de Empleados ===")
  print ("1. Añadir empleado")
  print ("2. Listar empleados")
  print ("3. Buscar empleado por nombre")
  print ("4. Subir salario a un empleado")
  print ("5. Mostrar gasto total en salarios")
  print ("6. Salir y guardar")

  opcion = input("Opcion: ").strip()

  if opcion == "1":
    nombre = input("Dime el nombre del empleado: ").strip()
    salario = float(input("Dime el salario del empleado: "))

    tipo = input("Tipo (1=Programador, 2=Diseñador): ").strip()
    if tipo == "1":
      emp = Programador(nombre, salario, input("Lenguaje: ").strip())
    else:
      emp = Diseñador(nombre, salario, input("Herramienta: ").strip())

    if empresa.añadir(emp):
      print(f"Añadido: {emp.nombre}")
    else:
      print(f"Ya existe un empleado llamado '{emp.nombre}'.")

  elif opcion == "2":
    empleados = empresa.listar()
    if not empleados:
      print ("No hay empleados registrados.")
    else:
      for e in empleados:
        e.mostrar_info()

  elif opcion == "3":
    emp = empresa.buscar(input("Nombre del empleado que quieres buscar: ").strip())
    if emp:
      emp.mostrar_info()
    else:
      print("Empleado no encontrado ")

  elif opcion == "4":
    emp = empresa.buscar(input("Dime el nombre del empleado que quieres buscar: ").strip())
    if emp is None:
      print("Empleado no encontrado")
    else:
      pct = float(input("Porcentaje a subir: "))
      emp.subir_salario(pct)
      print (f"Nuevo salario de {emp.nombre}: {emp.salario}")

  elif opcion == "5":
    print (f"Gasto total en salarios: {empresa.gastoTotal()}")

  elif opcion == "6":
    print ("Saliendo...")
    break

  else:
    print("Opción no válida. Elige de 1 a 6.")