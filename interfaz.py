import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import img2pdf

# Función para centrar la ventana
def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Función para seleccionar carpeta
def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    if carpeta:
        entry_carpeta.delete(0, tk.END)
        entry_carpeta.insert(0, carpeta)

# Función para gestionar la selección de Internas
def seleccionar_internas(opcion):
    if opcion == "CCITT Group 4":
        messagebox.showwarning("Aviso", "Las imágenes internas deben estar en blanco y negro para CCITT Group 4.")
    opcion_internas.set(opcion)

# Función para gestionar la compresión JPEG
def toggle_compresion_jpeg(tipo):
    if tipo == "portada":
        if compresion_jpeg_portada.get():
            spin_calidad_jpeg_portada.config(state=tk.NORMAL)
        else:
            spin_calidad_jpeg_portada.config(state=tk.DISABLED)
    elif tipo == "contraportada":
        if compresion_jpeg_contraportada.get():
            spin_calidad_jpeg_contraportada.config(state=tk.NORMAL)
        else:
            spin_calidad_jpeg_contraportada.config(state=tk.DISABLED)

# Función para actualizar la barra de progreso
def actualizar_progreso(valor, texto=None):
    if texto:
        progress_label.config(text=texto)
    progress_bar['value'] = valor
    root.update_idletasks()

# Función para convertir imágenes a PDF
def convertir_imagenes_a_pdf(input_folder, output_folder, dpi, formato, calidad_jpeg=None):
    imagenes = []
    for archivo in sorted(os.listdir(input_folder)):
        if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
            ruta_imagen = os.path.join(input_folder, archivo)
            if calidad_jpeg is not None:
                img = Image.open(ruta_imagen)
                img.save(ruta_imagen, quality=calidad_jpeg, optimize=True)
            imagenes.append(ruta_imagen)
    
    if not imagenes:
        raise ValueError("No se encontraron imágenes en la carpeta 'input'.")

    pdf_output = os.path.join(output_folder, "output.pdf")
    with open(pdf_output, "wb") as f:
        if formato == "CCITT Group 4":
            imagenes_pil = [Image.open(img).convert('1') for img in imagenes]  # Convertir a B/N
            f.write(img2pdf.convert(imagenes_pil))
        else:
            f.write(img2pdf.convert(imagenes))

# Función principal para procesar imágenes
def procesar():
    root_folder = entry_carpeta.get()
    
    if not root_folder or not os.path.isdir(root_folder):
        messagebox.showerror("Error", "Seleccione una carpeta válida.")
        return

    try:
        dpi_portadas = int(spin_dpi_portada.get())
        dpi_contraportadas = int(spin_dpi_contraportada.get())
        formato_internas = opcion_internas.get()
        calidad_jpeg_portada = int(spin_calidad_jpeg_portada.get()) if compresion_jpeg_portada.get() else None
        calidad_jpeg_contraportada = int(spin_calidad_jpeg_contraportada.get()) if compresion_jpeg_contraportada.get() else None

        # Validaciones
        if dpi_portadas < 150 or dpi_portadas > 1200 or dpi_contraportadas < 150 or dpi_contraportadas > 1200:
            raise ValueError("Los valores de DPI deben estar entre 150 y 1200.")
        if calidad_jpeg_portada and (calidad_jpeg_portada < 25 or calidad_jpeg_portada > 100):
            raise ValueError("La calidad JPEG para Portadas debe estar entre 25 y 100.")
        if calidad_jpeg_contraportada and (calidad_jpeg_contraportada < 25 or calidad_jpeg_contraportada > 100):
            raise ValueError("La calidad JPEG para Contraportadas debe estar entre 25 y 100.")

        carpetas_procesadas = 0
        carpetas_totales = sum(1 for folder_name in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, folder_name)))
        
        for i, folder_name in enumerate(os.listdir(root_folder)):
            folder_path = os.path.join(root_folder, folder_name)
            if os.path.isdir(folder_path):
                input_folder = os.path.join(folder_path, 'input')
                output_folder = os.path.join(folder_path, 'output')

                if os.path.exists(input_folder) and os.path.exists(output_folder):
                    actualizar_progreso((i + 1) / carpetas_totales * 100, f"Procesando: {folder_name}...")
                    
                    # Procesar portadas
                    portadas_folder = os.path.join(input_folder, 'portadas')
                    if os.path.exists(portadas_folder):
                        convertir_imagenes_a_pdf(portadas_folder, output_folder, dpi_portadas, "Portadas", calidad_jpeg_portada)
                    
                    # Procesar internas
                    internas_folder = os.path.join(input_folder, 'internas')
                    if os.path.exists(internas_folder):
                        convertir_imagenes_a_pdf(internas_folder, output_folder, dpi_portadas, formato_internas)
                    
                    # Procesar contraportadas
                    contraportadas_folder = os.path.join(input_folder, 'contraportadas')
                    if os.path.exists(contraportadas_folder):
                        convertir_imagenes_a_pdf(contraportadas_folder, output_folder, dpi_contraportadas, "Contraportadas", calidad_jpeg_contraportada)
                    
                    carpetas_procesadas += 1

        actualizar_progreso(100, "Procesamiento completado.")
        messagebox.showinfo("Completado", f"Se procesaron {carpetas_procesadas} carpetas.")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")
        actualizar_progreso(0, "Error en el procesamiento.")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Conversor de Imágenes a PDF")
centrar_ventana(root, 620, 400)

# Frame principal
main_frame = tk.Frame(root)
main_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Frame para la selección de carpeta
frame_carpeta = tk.Frame(main_frame)
frame_carpeta.pack(fill=tk.X, pady=5)
tk.Label(frame_carpeta, text="Carpeta raíz:").pack(side=tk.LEFT)
entry_carpeta = tk.Entry(frame_carpeta, width=40)
entry_carpeta.pack(side=tk.LEFT, padx=5)
tk.Button(frame_carpeta, text="Seleccionar", command=seleccionar_carpeta).pack(side=tk.LEFT)

# Frame contenedor de las secciones
frame_contenedor = tk.Frame(main_frame)
frame_contenedor.pack(pady=10)

# -------------------------- SECCIÓN PORTADAS --------------------------
frame_portadas = tk.LabelFrame(frame_contenedor, text="Portadas", padx=10, pady=10)
frame_portadas.pack(side=tk.LEFT, padx=10)

# DPI Portadas
tk.Label(frame_portadas, text="DPI (150-1200):").pack()
spin_dpi_portada = tk.Spinbox(frame_portadas, from_=150, to=1200, width=5)
spin_dpi_portada.delete(0, tk.END)
spin_dpi_portada.insert(0, "300")
spin_dpi_portada.pack()

# Compresión JPEG Portadas
compresion_jpeg_portada = tk.BooleanVar(value=False)
tk.Checkbutton(frame_portadas, text="Compresión JPEG", variable=compresion_jpeg_portada, 
              command=lambda: toggle_compresion_jpeg("portada")).pack(pady=5)
tk.Label(frame_portadas, text="Calidad (25-100):").pack()
spin_calidad_jpeg_portada = tk.Spinbox(frame_portadas, from_=25, to=100, width=5, state=tk.DISABLED)
spin_calidad_jpeg_portada.pack()

# -------------------------- SECCIÓN INTERNAS --------------------------
frame_internas = tk.LabelFrame(frame_contenedor, text="Internas", padx=10, pady=10)
frame_internas.pack(side=tk.LEFT, padx=10)
opcion_internas = tk.StringVar(value="Sin procesar")
tk.Radiobutton(
    frame_internas, 
    text="Sin procesar", 
    variable=opcion_internas, 
    value="Sin procesar",
    command=lambda: seleccionar_internas("Sin procesar")
).pack()
tk.Radiobutton(
    frame_internas, 
    text="CCITT Group 4", 
    variable=opcion_internas, 
    value="CCITT Group 4",
    command=lambda: seleccionar_internas("CCITT Group 4")
).pack()

# ----------------------- SECCIÓN CONTRAPORTADAS -----------------------
frame_contraportadas = tk.LabelFrame(frame_contenedor, text="Contraportadas", padx=10, pady=10)
frame_contraportadas.pack(side=tk.LEFT, padx=10)

# DPI Contraportadas
tk.Label(frame_contraportadas, text="DPI (150-1200):").pack()
spin_dpi_contraportada = tk.Spinbox(frame_contraportadas, from_=150, to=1200, width=5)
spin_dpi_contraportada.delete(0, tk.END)
spin_dpi_contraportada.insert(0, "300")
spin_dpi_contraportada.pack()

# Compresión JPEG Contraportadas
compresion_jpeg_contraportada = tk.BooleanVar(value=False)
tk.Checkbutton(frame_contraportadas, text="Compresión JPEG", variable=compresion_jpeg_contraportada,
              command=lambda: toggle_compresion_jpeg("contraportada")).pack(pady=5)
tk.Label(frame_contraportadas, text="Calidad (25-100):").pack()
spin_calidad_jpeg_contraportada = tk.Spinbox(frame_contraportadas, from_=25, to=100, width=5, state=tk.DISABLED)
spin_calidad_jpeg_contraportada.pack()

# Botón de inicio
tk.Button(main_frame, text="Iniciar", command=procesar).pack(pady=10)

# Barra de progreso
frame_progreso = tk.Frame(main_frame)
frame_progreso.pack(fill=tk.X, pady=10)
progress_label = tk.Label(frame_progreso, text="", anchor=tk.CENTER)
progress_label.pack(fill=tk.X)
progress_bar = ttk.Progressbar(frame_progreso, orient=tk.HORIZONTAL, length=580, mode="determinate")
progress_bar.pack(fill=tk.X)

root.mainloop()