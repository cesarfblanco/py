listaMonedas = ["De $ a €","De € a $","De $ a Bs","De € a Bs"]


while True:
    for x, y in enumerate(listaMonedas):
        print(f"{x}.- {y}")

    try:
        opcionDivisaUsuario = int(input("Seleccione entre las opciones: "))

        if opcionDivisaUsuario < 0 or opcionDivisaUsuario > len(listaMonedas) -1:
            print("Ingrese una opcion valida")
        else:
            divisaUsuario = float(input("Ingrese la cantidad que quiere convertir: "))
            if divisaUsuario < 0:
                print("Ingrese una cantidad valida")
            else:
                if opcionDivisaUsuario == 0:
                    totalCambio = divisaUsuario * 0.85
                    print(f"Cambio realizado usted disponde ahora de {totalCambio}€")
                    break
                elif opcionDivisaUsuario == 1:
                    totalCambio = divisaUsuario * 1.15
                    print(f"Cambio realizado usted disponde ahora de {totalCambio}$")
                    break
                elif opcionDivisaUsuario == 3:
                    totalCambio = divisaUsuario * 42.52
                    print(f"Cambio realizado usted disponde ahora de {totalCambio}Bs")
                    break
                elif opcionDivisaUsuario == 2:
                    totalCambio = divisaUsuario * 38.88
                    print(f"Cambio realizado usted disponde ahora de {totalCambio:.2f} Bs")
                    break
    except ValueError:
        print("Ingrese un numero valido")










