
from tabulate import tabulate
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


