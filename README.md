## Índice
- [Introducción](#Introducción)
- [Requisitos](#Requisitos)
  - [Hardware](#Hardware)
  - [Software](#Software)
- [Guías y Tutoriales](#Guias-y-Tutoriales)
  - [Escaneo de partituras](#cost-estimation)
    - [Convención de nombres de archivos](#github-codespaces)
  - [Postprocesamiento de Imágenes](#cost-estimation)
  - [Automatización del Proceso](#Guias-y-Tutoriales)
- [Scripts y herramientas para facilitar el flujo de trabajo](#github-codespaces)
- [Almacenamiento y Publicación](#Guias-y-Tutoriales)
    - [Organización de archivos en la nube](#github-codespaces)
    - [Acceso y consulta en línea](#github-codespaces)
    - [Licencias y derechos de autor](#github-codespaces)
- [Contribuir al Proyecto](#Guias-y-Tutoriales)
    - [Cómo colaborar y aportar mejoras](#github-codespaces)
    - [Reporte de errores y sugerencias](#github-codespaces)
  
## Introducción 
Este repositorio ofrece una solución innovadora para el escaneo y procesamiento de partituras, automatizando la generación de archivos PDF a partir de imágenes. Diseñado para músicos, educadores y entusiastas de la música, este proyecto simplifica la digitalización de partituras, permitiendo una conversión rápida y precisa a formatos listos para imprimir o compartir.
## Requisitos
### Hardware
Para garantizar el mejor rendimiento y compatibilidad con este proyecto, se recomienda utilizar los siguientes dispositivos de hardware:

Escáneres recomendados:

* Xerox DocuMate 4700: Un escáner robusto con una resolución de hasta 1200 DPI, ideal para digitalizar partituras sueltas y portadas con gran precisión y calidad.

* CZUR ET24 Pro: Un escáner inteligente con funciones avanzadas, perfecto para la captura de imágenes de libros encuadernados o empastados. Su tecnología permite un escaneo rápido y eficiente, incluso para documentos difíciles de manipular
  
Si no cuentas con los escáneres mencionados, puedes utilizar las siguientes opciones:

* Otros modelos de escáneres:
Cualquier escáner con una resolución mínima de 300 DPI y funcionalidades básicas de digitalización puede ser compatible. Asegúrate de que el escáner permita ajustes de brillo, contraste y formato de salida (por ejemplo, JPEG, TIF, PNG).

* Cámara digital de alta resolución:
Una cámara con una resolución mínima de 12 MP y un trípode para estabilidad puede ser una excelente alternativa. Recomendamos utilizar iluminación adecuada y un fondo uniforme para garantizar capturas nítidas y consistentes.


### Software

Software básico de Windows:

* Visor de Fotos: Para visualizar y organizar las imágenes escaneadas o capturadas.

* Paint: Para realizar ediciones simples, como recortes o ajustes básicos.

Software de postprocesamiento:

* GIMP (GNU Image Manipulation Program): Una herramienta de software libre ideal para ediciones más avanzadas, como corrección de colores, recorte preciso y eliminación de imperfecciones.

Software de los escáneres:

Utiliza el software predeterminado que viene con tu escáner (por ejemplo, Xerox o CZUR) para configurar y optimizar el proceso de escaneo.

Generación automática de PDFs:

* Python: Se utiliza para automatizar la creación de archivos PDF a partir de las imágenes procesadas. Se recomienda el uso de bibliotecas como Pillow y img2pdf.

### Configuración recomendada del sistema
Para este proyecto

## Guias-y-Tutoriales


# Scripts y herramientas para facilitar el flujo de trabajo
## PortadaExtractor.py
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

## RenameIamges.py
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

## RenameIamgesBatch.py
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
