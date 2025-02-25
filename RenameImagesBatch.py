import os
import re

def extraer_numero(nombre):
    match = re.search(r"\((\d+)([A-Z]?)\)", nombre, re.IGNORECASE)
    if match:
        numero = int(match.group(1))
        letra = match.group(2).upper() if match.group(2) else ""
        return (numero, letra)
    return (float('inf'), "")

def renombrar_imagenes(directorio):
    imagenes = sorted(
        [f for f in os.listdir(directorio) if f.lower().endswith(('jpg', 'jpeg', 'png', 'tif'))],
        key=extraer_numero
    )

    contador = 1
    for imagen in imagenes:
        ruta_origen = os.path.join(directorio, imagen)
        
        if "portada" in imagen.lower():
            continue  # Mantener el nombre de la portada
        
        extension = os.path.splitext(imagen)[1].lower()
        nuevo_nombre = f"imagen{contador:03d}{extension}"
        ruta_destino = os.path.join(directorio, nuevo_nombre)

        # Solo renombrar si el nombre es diferente
        if ruta_origen != ruta_destino:
            os.rename(ruta_origen, ruta_destino)
            print(f"{imagen} -> {nuevo_nombre}")

        contador += 1

def buscar_y_procesar_subcarpetas():
    directorio_base = os.getcwd()
    
    for carpeta in os.listdir(directorio_base):
        ruta_carpeta = os.path.join(directorio_base, carpeta)
        
        if os.path.isdir(ruta_carpeta):
            ruta_input = os.path.join(ruta_carpeta, "input")
            
            if os.path.isdir(ruta_input):
                print(f"\nProcesando imágenes en: {ruta_input}")  # ✅ Solo la ruta completa
                renombrar_imagenes(ruta_input)

# Ejecutar el proceso
buscar_y_procesar_subcarpetas()
