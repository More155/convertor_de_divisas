
def obtener_monto_ars() -> float:
    """
    Solicita al usuario un monto en pesos argentinos y valida la entrada.

    Returns:
        float: El monto ingresado por el usuario en formato numérico.
    """
    while True:
        entrada = input("Ingrese el monto en pesos argentinos (ARS) a convertir: ")

        try:
            monto = float(entrada.replace(",", "."))

            if monto == 0:
                print("⚠️  Ingrese un monto mayor a 0.")
                continue

            elif monto < 0:
                print("⚠️   Por favor, ingrese un monto positivo.")
                continue

            return monto

        except ValueError:
            print("❌ Error: Ingrese un valor numérico válido (ej: 15000 o 15000.50).")

