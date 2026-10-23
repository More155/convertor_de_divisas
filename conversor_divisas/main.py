
from getApi import consultar_api_dolar
from func.obtener_monto_ars import obtener_monto_ars
from func.procesar_cotizaciones import procesar_cotizaciones
from func.mostrar_resultados import mostrar_resultados


def main() -> None:
    print("=" * 40)
    print("💰 CONVERSOR DE DIVISAS 💰")
    print("=" * 40)

    monto = obtener_monto_ars()
    # Consultar las cotizaciones
    print("\nConsultando cotizaciones actuales...")

    cotizaciones = consultar_api_dolar()

    # Procesar los datos
    datos_tabla = procesar_cotizaciones(
        monto,
        cotizaciones
    )

    # Mostrar los resultados
    mostrar_resultados(datos_tabla)


if __name__ == "__main__":
    main()
