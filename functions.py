from playwright.sync_api import sync_playwright
import os, pandas as pd, re

def escrapear(url, pag, max_pags):
    with sync_playwright() as p:

        # Browser con palywright
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url) 


        items = []
        while pag <= max_pags:
            # 1. Utilizamos locator ya que espera sola a que este disponible la etiqueta
            cards = page.locator(".ui-search-layout__item")
            
            # 2. Esperamos a que al menos uno sea visible (auto-waiting)
            cards.first.wait_for()

            # 3. Iteramos usando locators
            count = cards.count()
            for i in range(count):
                quote = cards.nth(i)

                try:
                     # Usamos .inner_text() directamente sobre el locator
                     # Playwright esperará a que el texto aparezca
                    titulo = quote.locator(".poly-component__title").inner_text(timeout=2000)
                    precio = quote.locator(".poly-component__price .andes-money-amount__fraction").first.inner_text(timeout=2000)

                    items.append({
                        "nombre_producto": titulo,
                        "precio": precio
                    })

                except Exception as e:
                    print(f"Error en producto {i}: {e}")
                    continue # Salta al siguiente producto
                
            # 4. Localizamos el botón "Siguiente" por su título
            next_button = page.get_by_title("Siguiente")

            # 5. Verificamos si es visible y hacemos clic
            if next_button.is_visible():
                next_button.click()
                # Opcional: esperar a que la página cambie o cargue el nuevo contenido
                page.wait_for_load_state("networkidle")

                pag += 1 # Incrementamos el contador
            else:
                break
        print(f"Total extraído: {len(items)} items.")
        browser.close()

        return items


def exportar(lista, carpeta_salida):
    try:
        # Creamos la carpeta de salida
        os.makedirs(carpeta_salida, exist_ok=True)
    
        # Creamos la ruta final del csv
        ruta_final = os.path.join(carpeta_salida, "productos.csv")

        # Creamos el df
        df = pd.DataFrame(lista)

        # Limpiamos el df
        df["nombre_producto"] = df["nombre_producto"].str.strip().astype(str)
        
        # LIMPIEZA DE LA COLUMNA PRECIO
        # [^\d.,]: Busca cualquier carácter que no sea dígito (\d), punto (.) o coma (,) y lo borra
        df['precio'] = df['precio'].str.replace(r'[^\d.,]', '', regex=True)

        # Exportamos el df
        df.to_csv(ruta_final, index=True, encoding='utf-8-sig')
    except Exception as e:
        print(f"Error con la exportacion: {e}")
    
