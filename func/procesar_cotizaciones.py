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

