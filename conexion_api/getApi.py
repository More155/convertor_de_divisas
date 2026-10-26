
import sys
import requests


def consultar_api_dolar() -> list[dict]:
    """
    Realiza una petición HTTP a DolarAPI para obtener las cotizaciones.

    Returns:
        list[dict]: Lista de diccionarios con los datos de cada tipo de dólar.
    """
    url = "https://dolarapi.com/v1/dolares"

    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
        datos = respuesta.json()

        if not isinstance(datos, list):
            raise ValueError(
                "El formato de respuesta de la API cambió inesperadamente."
            )

        return datos

    except requests.exceptions.Timeout:
        print("❌ Error: La conexión a la API tardó demasiado (Timeout).")
        sys.exit(1)

    except requests.exceptions.ConnectionError:
        print("❌ Error: No hay conexión a Internet o la API está caída.")
        sys.exit(1)

    except requests.exceptions.HTTPError as err_http:
        print(f"❌ Error HTTP al consultar la API: {err_http}")
        sys.exit(1)

    except ValueError as err_val:
        print(f"❌ Error en los datos recibidos: {err_val}")
        sys.exit(1)

    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        sys.exit(1)
