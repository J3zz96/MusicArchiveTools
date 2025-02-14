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
        
        nuevo_nombre = f"imagen{contador:03d}{os.path.splitext(imagen)[1]}"
        contador += 1
        
        ruta_destino = os.path.join(directorio, nuevo_nombre)
        os.rename(ruta_origen, ruta_destino)
        print(f"{imagen} -> {nuevo_nombre}")

# Uso
directorio_base = os.getcwd()
renombrar_imagenes(directorio_base)
