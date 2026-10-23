import sys
import requests
from tabulate import tabulate


def obtener_monto_ars() -> float:
    """
    Solicita al usuario un monto en pesos argentinos y valida la entrada.
    
    Returns:
        float: El monto ingresado por el usuario en formato numérico.
    """
    while True:
        entrada = input("Ingrese el monto en pesos argentinos (ARS) a convertir: ")
        try:
            # Reemplaza coma por punto para evitar errores comunes de tipeo
            monto = float(entrada.replace(",", "."))
            if monto < 0:
                print("⚠️  Por favor, ingrese un monto positivo.")
                continue
            return monto
        except ValueError:
            print("❌ Error: Ingrese un valor numérico válido (ej: 15000 o 15000.50).")


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
            raise ValueError("El formato de respuesta de la API cambió inesperadamente.")
            
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


def procesar_cotizaciones(monto_ars: float, cotizaciones: list[dict]) -> list[list]:
    """
    Filtra el dólar Oficial y Blue, y calcula la conversión.
    
    Args:
        monto_ars (float): Monto original en pesos argentinos.
        cotizaciones (list[dict]): Datos JSON obtenidos de la API.
        
    Returns:
        list[list]: Datos estructurados en filas para la tabla.
    """
    datos_tabla = []
    
    for cotizacion in cotizaciones:
        casa = cotizacion.get("casa")
        
        if casa in ["oficial", "blue"]:
            nombre = cotizacion.get("nombre", "Desconocido")
            compra = cotizacion.get("compra", 0.0)
            venta = cotizacion.get("venta", 0.0)
            
            try:
                # Para comprar USD, el usuario paga el valor de "venta"
                if venta > 0:
                    total_convertido = monto_ars / venta
                else:
                    total_convertido = 0.0
                    
                datos_tabla.append([
                    nombre,
                    f"${compra}",
                    f"${venta}",
                    f"USD {total_convertido:.2f}"
                ])
            except (TypeError, ZeroDivisionError) as e:
                print(f"⚠️  Error al procesar los datos de {nombre}: {e}")
                
    return datos_tabla


def mostrar_resultados(datos_tabla: list[list]) -> None:
    """
    Imprime los resultados en consola utilizando la librería tabulate.
    
    Args:
        datos_tabla (list[list]): Filas con la información a mostrar.
    """
    if not datos_tabla:
        print("⚠️  No se encontraron datos del Dólar Oficial o Blue.")
        return

    encabezados = ["Tipo de Dólar", "Precio Compra", "Precio Venta", "Total Convertido"]
    # tablefmt="fancy_grid" genera bordes redondeados y prolijos
    tabla = tabulate(datos_tabla, headers=encabezados, tablefmt="fancy_grid")
    
    print("\n" + tabla + "\n")


def main() -> None:
    """
    Función principal que orquesta el flujo del programa.
    """
    print("=" * 40)
    print("💰 CONVERSOR DE DIVISAS (EN VIVO) 💰")
    print("=" * 40)
    
    monto = obtener_monto_ars()
    
    print("\nConsultando cotizaciones actuales...")
    cotizaciones_crudas = consultar_api_dolar()
    
    datos_procesados = procesar_cotizaciones(monto, cotizaciones_crudas)
    
    mostrar_resultados(datos_procesados)


if __name__ == "__main__":
    main()