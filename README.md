MercadoLibre Scraper Python
 Este proyecto es una herramienta de automatización diseñada para extraer información de productos (títulos y precios) desde MercadoLibre de forma eficiente. Utiliza técnicas modernas de web scraping para navegar por sitios dinámicos y procesar los datos obtenidos.

Características
 Extracción Automatizada: Navegación por múltiples páginas de resultados.

 Manejo de Contenido Dinámico: Uso de Playwright para gestionar sitios con renderizado de JavaScript.

 Limpieza de Datos: Procesamiento y estructuración de la información mediante Pandas.

 Exportación Flexible: Generación de archivos listos para análisis (CSV/Excel).


Tecnologías utilizadas
 Lenguaje: Python 3.10+

 Librerías principales: * Playwright (Navegación y scraping)

 Pandas (Manipulación y limpieza de datos)

 OS / Glob (Gestión de rutas de archivos)


Requisitos previos
 Es necesario tener instalado Python y el navegador para Playwright en tu sistema (ej. Ubuntu):

Bash
 pip install playwright pandas
 playwright install chromium


Uso
 Clona el repositorio.

Ejecuta el script principal:

Bash
python scraper.py
El resultado se guardará automáticamente en la carpeta de resultados (ignorada por git).
