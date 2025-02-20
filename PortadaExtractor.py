import os
import shutil

def obtener_nombre_portada(carpeta):
    """Extrae el nombre hasta 'Apellidos, Nombres -' y agrega 'portada de Título', omitiendo la editorial."""
    partes = carpeta.split(' - ')
    if len(partes) < 2:
        return None  # Evita errores si el nombre no tiene el formato esperado
    titulo = partes[1].split('.')[0]  # Omite la editorial
    return f"{partes[0]} - portada de {titulo}"

def mover_portadas():
    directorio_actual = os.getcwd()
    carpeta_portadas = os.path.join(directorio_actual, "portadas")
    os.makedirs(carpeta_portadas, exist_ok=True)
    
    for carpeta in os.listdir(directorio_actual):
        carpeta_path = os.path.join(directorio_actual, carpeta)
        
        if os.path.isdir(carpeta_path):
            input_path = os.path.join(carpeta_path, "input")
            if os.path.exists(input_path):
                for extension in [".jpg", ".tif"]:
                    portada_path = os.path.join(input_path, f"portada{extension}")
                    if os.path.exists(portada_path):
                        nuevo_nombre = obtener_nombre_portada(carpeta)
                        if nuevo_nombre:
                            nuevo_path = os.path.join(carpeta_portadas, f"{nuevo_nombre}{extension}")
                            shutil.copy(portada_path, nuevo_path)
                            print(f"Portada copiada: {nuevo_path}")
                        break  # Si encontró una, no busca otra

if __name__ == "__main__":
    mover_portadas()
