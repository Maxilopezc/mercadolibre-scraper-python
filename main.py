from functions import escrapear, exportar
import os

def main():
    # Direccion de nuestra carpeta
    carpeta_origen = os.path.dirname(os.path.abspath(__file__))

    # Creamos la direccion de la carpeta de salida
    carpeta_salida = os.path.join(carpeta_origen, "productos_mercadolibre")

    # Url
    url = "https://listado.mercadolibre.cl/cadenas-de-plata-hombre#D[A:cadenas%20de%20plata%20hombre]"

    # Maximo de paginas (por seguridad)
    pag = 1
    max_pags = 10

    # Lista y DataFrame de los productos obtenidos
    lista = escrapear(url, pag, max_pags)
    exportar(lista, carpeta_salida)

if __name__ == "__main__":
    main()