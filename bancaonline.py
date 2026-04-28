saldo=0
while True:
  print(""" 1. Ingresar dinero
            2. Retirar dinero
            3. Consultar saldo
            4. Reiniciar cuenta
            5. Salir """)
  opcion = int(input("Introduce una opción:"))

  if opcion == 1:
    ingresar = float(input("Indica la cantidad a ingresar: "))
    saldo += ingresar
    print(f"Has ingresado tu dinero")
