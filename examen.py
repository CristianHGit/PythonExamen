usuario = "LCR-3333"
contraseña = "12345"

intentos_login = 3
while intentos_login > 0:
    print("Ingrese su usuario (tiene", intentos_login, "intentos restantes):")
    usuario_input = input()
    print("Ingrese su contraseña:")
    contraseña_input = input()
    
    if usuario_input == usuario and contraseña_input == contraseña:
        print("¡Usuario y contraseña correctos! Puede ingresar.")
        break
    else:
        print("Usuario o contraseña incorrectos.")
        intentos_login -= 1

if intentos_login == 0:
    print("Ha excedido el número máximo de intentos de inicio de sesión.")
else:
    while True:
        print("Ingrese lo que quiera realizar:")
        print("1. Retirar")
        print("2. Depositar")
        print("3. Transferencia")
        print("4. Estado de cuenta")
        print("5. Salir")
        opcion = int(input())
        
        if opcion == 1:
            print("Elija una opción de retiro:")
            print("1. Efectivo")
            print("2. Cheque")
            print("3. Tarjeta")
            print("4. Transferencia")
            print("5. Salir")
            opcion_retiro = int(input("Ingrese el número correspondiente a su elección: "))
            if opcion_retiro == 1:
                cantidad = int(input("Ingrese la cantidad a retirar en efectivo: "))
                print("Ha retirado", cantidad, "en efectivo.")
            elif opcion_retiro == 5:
                print("¡Hasta luego!")
                break
            else:
                print("Opción de retiro no válida.")
        elif opcion == 5:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
