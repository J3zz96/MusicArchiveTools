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
    - 📂 Apellido, Nombre - Título. Editorial
        - 📂 input
          - Escanear oct. 01, 2024 (1).TIF -> imagen001.TIF
          - Escanear oct. 01, 2024 (2).TIF -> imagen002.TIF
          - Escanear oct. 01, 2024 (3).TIF -> imagen003.TIF
          - Escanear oct. 01, 2024 (4).TIF -> imagen004.TIF
           - Escanear oct. 01, 2024 (5).TIF -> imagen005.TIF
          - Escanear oct. 01, 2024 (6).TIF -> imagen006.TIF
          - Escanear oct. 01, 2024 (6A).TIF -> imagen007.TIF
          - portada.TIF -> portada.TIF
    - 📂 Apellido, Nombre - Título. Editorial
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
