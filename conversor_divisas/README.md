# 📚 Conversor de Divisas (Cotización en vivo)

Este es un programa de consola desarrollado en Python que permite a los usuarios ingresar un monto en Pesos Argentinos (ARS) y calcular su equivalente en Dólar Oficial y Dólar Blue. 

El proyecto consume datos en tiempo real mediante una API pública ([DolarAPI](https://dolarapi.com/)) y muestra los resultados de manera estilizada en una tabla

## Integrantes del Grupo
- Morena Nicora
- Agustin Sanchez
- Luciano Esquivel


## Instalación y Configuración

1. **Clonar o descargar el proyecto** y abrir una terminal en la carpeta principal.

2. **Ingresar a la carpeta del proyecto:**
   
   cd conversor_divisas

3. **Crear el entorno virtual:**

    python -m venv .venv

4. **Activar el entorno virtual:**
     En Linux/Mac:
    source .venv/bin/activate

     En Windows:
    .\.venv\Scripts\activate

5. **Instalar las dependencias requeridas:**
    
    pip install -r requirements.txt

6. **Ejecución:**
     Con el entorno virtual activado y asegurándote de estar dentro de la carpeta conversor_divisas, ejecuta:

    python main.py