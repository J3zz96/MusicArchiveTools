## Índice
- [Introducción](#Introducción)

¿Qué es este repositorio?
Objetivo del proyecto (digitalización y catalogación de partituras)
¿Para quién está dirigido?
Requisitos

Hardware necesario (escáneres recomendados, cámara, etc.)
Software requerido (escáner, edición de imágenes, OCR, OMR)
Configuración recomendada del sistema
Guías y Tutoriales

📖 Escaneo de Partituras
Preparación de documentos
Configuración del escáner
Formatos de archivo recomendados
Flujo de trabajo óptimo
🖼 Postprocesamiento de Imágenes
Limpieza y mejora de calidad
Conversión a blanco y negro (CCITT Group 4)
Corrección de alineación y recorte
🎼 Digitalización Musical (OMR y OCR)
Reconocimiento de notación musical
Conversión a MusicXML
🗂 Organización y Catalogación
Convención de nombres de archivos
Uso de metadatos y etiquetas
Estructura del repositorio
Automatización del Proceso

Scripts y herramientas para facilitar el flujo de trabajo
Ejemplos de código y automatización
Almacenamiento y Publicación

Organización de archivos en la nube
Acceso y consulta en línea
Licencias y derechos de autor
Contribuir al Proyecto

Cómo colaborar y aportar mejoras
Reporte de errores y sugerencias
Referencias y Recursos Adicionales

Bibliografía y enlaces útiles




## Introducción 





# PortadaExtractor.py
Este script busca y copia todas las portadas dentro de la carpeta actual a una carpeta nueva llamada portadas (no es necesesario crear la carpeta de portadas)
- 📂 Carpeta actual (aquí se ejecuta el script)
    - 📂 APELLIDO, Nombre - Ejemplo. Editorial
        - 📂 input
          - Imagen001.TIF
          - Etc....
          - portada.TIF 
    - 📂 APELLIDO, Nombre - Otro ejemplo. Editorial
         - 📂 input
             - 📂 input
          - Imagen001.TIF
          - Etc....
          - portada.TIF 
    - 📂 Etc .......
- 📂 portadas ---> se crea esta nueva carpeta y aquí se copian todas las portadas que encontró el script
  - portada de APELLIDO, NOMBRE - Ejemplo
  - portada de APELLIDO, NOMBRE - Otro ejemplo

# RenameIamges.py
Este script busca en la carpeta actual y renombra las imagenes que salen por defecto en el escaner XEROX a imagen001, imagen002, etc... dejando 
con el mismo nombre a la portada (importante que ya exista la imagen con el nombre portada) 
aquí un ejemplo:
- Escanear oct. 01, 2024 (1).TIF -> imagen001.TIF
- Escanear oct. 01, 2024 (2).TIF -> imagen002.TIF
- Escanear oct. 01, 2024 (3).TIF -> imagen003.TIF
- Escanear oct. 01, 2024 (4).TIF -> imagen004.TIF
- Escanear oct. 01, 2024 (5).TIF -> imagen005.TIF
- Escanear oct. 01, 2024 (6).TIF -> imagen006.TIF
- Escanear oct. 01, 2024 (6A).TIF -> imagen007.TIF *
- Escanear oct. 01, 2024 (7).TIF -> imagen008.TIF
- etc........
- Escanear oct. 01, 2024 (30).TIF -> imagen031.TIF
- portada.TIF -> portada.TIF
  
Importante tomar en cuenta que toma los números internos en el parentesis así como las letras del abcedario como se muestra en el "*" 

# RenameIamgesBatch.py
Este script tomo como base el de RanameImages.py y lo ejecuta por lotes (Tienen que tener la carpeta de input para que funcione)

- 📂 Carpeta actual (aquí se ejecuta el script)
    - 📂 APELLIDO, Nombre - Título. Editorial
        - 📂 input
          - Escanear oct. 01, 2024 (1).TIF -> imagen001.TIF
          - Escanear oct. 01, 2024 (2).TIF -> imagen002.TIF
          - Escanear oct. 01, 2024 (3).TIF -> imagen003.TIF
          - Escanear oct. 01, 2024 (4).TIF -> imagen004.TIF
           - Escanear oct. 01, 2024 (5).TIF -> imagen005.TIF
          - Escanear oct. 01, 2024 (6).TIF -> imagen006.TIF
          - Escanear oct. 01, 2024 (6A).TIF -> imagen007.TIF
          - portada.TIF -> portada.TIF
    - 📂 APELLIDO, Nombre - Título. Editorial
         - 📂 input
            - Escanear oct. 01, 2024 (1).TIF -> imagen001.TIF
            - Escanear oct. 01, 2024 (2).TIF -> imagen002.TIF
            - Escanear oct. 01, 2024 (3).TIF -> imagen003.TIF
            - Escanear oct. 01, 2024 (4).TIF -> imagen004.TIF
             - Escanear oct. 01, 2024 (5).TIF -> imagen005.TIF
            - Escanear oct. 01, 2024 (6).TIF -> imagen006.TIF
            - Escanear oct. 01, 2024 (6A).TIF -> imagen007.TIF
            - portada.TIF -> portada.TIF
    - 📂 Etc .......
