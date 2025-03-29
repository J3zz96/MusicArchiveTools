import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ExifTags
import img2pdf
import re
from collections import defaultdict

# ------------------------- FUNCIONES DE PROCESAMIENTO -------------------------
def correct_exif_orientation(img):
    """Corrige la orientación de la imagen basada en metadatos EXIF."""
    try:
        if hasattr(img, '_getexif'):
            exif = img._getexif()
            if exif:
                for tag, value in exif.items():
                    if ExifTags.TAGS.get(tag) == 'Orientation':
                        if value == 3:
                            img = img.rotate(180, expand=True)
                        elif value == 6:
                            img = img.rotate(270, expand=True)
                        elif value == 8:
                            img = img.rotate(90, expand=True)
    except (AttributeError, KeyError, IndexError):
        pass
    return img

def convert_to_bw(img):
    """Convierte imagen a blanco y negro (1-bit) para CCITT Group 4."""
    return img.convert('L').point(lambda x: 0 if x < 128 else 255, '1')

def numerical_sort(filename):
    """Ordena archivos numéricamente para mantener secuencia."""
    numbers = re.findall(r'\d+', filename)
    return int(numbers[0]) if numbers else 0

def process_images(input_folder, output_folder, config):
    """Procesa imágenes según configuración de la interfaz."""
    files = {
        'portadas': [],
        'internas': [],
        'contraportadas': []
    }

    # Clasificar archivos
    for filename in sorted(os.listdir(input_folder), key=numerical_sort):
        lower_name = filename.lower()
        if 'portada' in lower_name and lower_name.endswith(('.jpg', '.jpeg', '.tif', '.tiff', '.png')):
            files['portadas'].append(filename)
        elif 'contraportada' in lower_name and lower_name.endswith(('.jpg', '.jpeg', '.tif', '.tiff', '.png')):
            files['contraportadas'].append(filename)
        elif lower_name.endswith(('.jpg', '.jpeg', '.tif', '.tiff', '.png')):
            files['internas'].append(filename)

    optimized = []

    # Procesar portadas
    for filename in files['portadas']:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"opt_{os.path.splitext(filename)[0]}.jpg")
        try:
            with Image.open(input_path) as img:
                img = correct_exif_orientation(img)
                img.save(output_path, 'JPEG', 
                         quality=config['calidad_jpeg_portada'] or 85,
                         dpi=(config['dpi_portadas'], config['dpi_portadas']))
                optimized.append(output_path)
        except Exception as e:
            print(f"Error procesando portada {filename}: {e}")

    # Procesar internas
    for filename in files['internas']:
        input_path = os.path.join(input_folder, filename)
        ext = 'tif' if config['formato_internas'] == 'CCITT Group 4' else 'jpg'
        output_path = os.path.join(output_folder, f"opt_{os.path.splitext(filename)[0]}.{ext}")
        try:
            with Image.open(input_path) as img:
                img = correct_exif_orientation(img)
                if config['formato_internas'] == 'CCITT Group 4':
                    img = convert_to_bw(img)
                    img.save(output_path, 'TIFF', compression='group4',
                             dpi=(config['dpi_internas'], config['dpi_internas']))
                else:
                    img.save(output_path, 'JPEG', 
                             quality=85,
                             dpi=(config['dpi_internas'], config['dpi_internas']))
                optimized.append(output_path)
        except Exception as e:
            print(f"Error procesando interna {filename}: {e}")

    # Procesar contraportadas
    for filename in files['contraportadas']:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"opt_{os.path.splitext(filename)[0]}.jpg")
        try:
            with Image.open(input_path) as img:
                img = correct_exif_orientation(img)
                img.save(output_path, 'JPEG', 
                         quality=config['calidad_jpeg_contraportada'] or 85,
                         dpi=(config['dpi_contraportadas'], config['dpi_contraportadas']))
                optimized.append(output_path)
        except Exception as e:
            print(f"Error procesando contraportada {filename}: {e}")

    return optimized

def generar_pdf(imagenes, output_pdf):
    """Genera PDF desde lista de imágenes optimizadas."""
    try:
        with open(output_pdf, "wb") as f:
            f.write(img2pdf.convert([img for img in imagenes if os.path.exists(img)]))
        return True
    except Exception as e:
        print(f"Error generando PDF: {e}")
        return False

# ------------------------- INTERFAZ GRÁFICA -------------------------
class ConversorPDFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Imágenes a PDF")
        self.centrar_ventana(620, 400)
        
        # Variables de configuración
        self.opcion_internas = tk.StringVar(value="Sin procesar")
        self.compresion_jpeg_portada = tk.BooleanVar(value=False)
        self.compresion_jpeg_contraportada = tk.BooleanVar(value=False)
        
        self.crear_interfaz()
    
    def centrar_ventana(self, ancho, alto):
        pantalla_ancho = self.root.winfo_screenwidth()
        pantalla_alto = self.root.winfo_screenheight()
        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")
    
    def crear_interfaz(self):
        # Frame principal
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        # Selección de carpeta
        frame_carpeta = tk.Frame(main_frame)
        frame_carpeta.pack(fill=tk.X, pady=5)
        
        tk.Label(frame_carpeta, text="Carpeta raíz:").pack(side=tk.LEFT)
        self.entry_carpeta = tk.Entry(frame_carpeta, width=40)
        self.entry_carpeta.pack(side=tk.LEFT, padx=5)
        tk.Button(frame_carpeta, text="Seleccionar", command=self.seleccionar_carpeta).pack(side=tk.LEFT)
        
        # Configuraciones
        frame_contenedor = tk.Frame(main_frame)
        frame_contenedor.pack(pady=10)
        
        # Sección Portadas
        frame_portadas = tk.LabelFrame(frame_contenedor, text="Portadas", padx=10, pady=10)
        frame_portadas.pack(side=tk.LEFT, padx=10)
        
        tk.Label(frame_portadas, text="DPI (150-1200):").pack()
        self.spin_dpi_portada = tk.Spinbox(frame_portadas, from_=150, to=1200, width=5)
        self.spin_dpi_portada.delete(0, tk.END)
        self.spin_dpi_portada.insert(0, "300")
        self.spin_dpi_portada.pack()
        
        tk.Checkbutton(frame_portadas, text="Compresión JPEG", 
                      variable=self.compresion_jpeg_portada,
                      command=lambda: self.toggle_compresion("portada")).pack(pady=5)
        
        tk.Label(frame_portadas, text="Calidad (25-100):").pack()
        self.spin_calidad_portada = tk.Spinbox(frame_portadas, from_=25, to=100, width=5, state=tk.DISABLED)
        self.spin_calidad_portada.pack()
        
        # Sección Internas
        frame_internas = tk.LabelFrame(frame_contenedor, text="Internas", padx=10, pady=10)
        frame_internas.pack(side=tk.LEFT, padx=10)
        
        tk.Radiobutton(frame_internas, text="Sin procesar", 
                      variable=self.opcion_internas, value="Sin procesar",
                      command=lambda: self.seleccionar_internas("Sin procesar")).pack()
        
        tk.Radiobutton(frame_internas, text="CCITT Group 4", 
                      variable=self.opcion_internas, value="CCITT Group 4",
                      command=lambda: self.seleccionar_internas("CCITT Group 4")).pack()
        
        # Sección Contraportadas
        frame_contraportadas = tk.LabelFrame(frame_contenedor, text="Contraportadas", padx=10, pady=10)
        frame_contraportadas.pack(side=tk.LEFT, padx=10)
        
        tk.Label(frame_contraportadas, text="DPI (150-1200):").pack()
        self.spin_dpi_contraportada = tk.Spinbox(frame_contraportadas, from_=150, to=1200, width=5)
        self.spin_dpi_contraportada.delete(0, tk.END)
        self.spin_dpi_contraportada.insert(0, "300")
        self.spin_dpi_contraportada.pack()
        
        tk.Checkbutton(frame_contraportadas, text="Compresión JPEG", 
                      variable=self.compresion_jpeg_contraportada,
                      command=lambda: self.toggle_compresion("contraportada")).pack(pady=5)
        
        tk.Label(frame_contraportadas, text="Calidad (25-100):").pack()
        self.spin_calidad_contraportada = tk.Spinbox(frame_contraportadas, from_=25, to=100, width=5, state=tk.DISABLED)
        self.spin_calidad_contraportada.pack()
        
        # Botón de inicio
        tk.Button(main_frame, text="Iniciar Procesamiento", 
                 command=self.iniciar_procesamiento).pack(pady=10)
        
        # Barra de progreso
        frame_progreso = tk.Frame(main_frame)
        frame_progreso.pack(fill=tk.X, pady=10)
        
        self.progress_label = tk.Label(frame_progreso, text="Esperando inicio...", anchor=tk.CENTER)
        self.progress_label.pack(fill=tk.X)
        
        self.progress_bar = ttk.Progressbar(frame_progreso, orient=tk.HORIZONTAL, length=580, mode="determinate")
        self.progress_bar.pack(fill=tk.X)
    
    def seleccionar_carpeta(self):
        carpeta = filedialog.askdirectory()
        if carpeta:
            self.entry_carpeta.delete(0, tk.END)
            self.entry_carpeta.insert(0, carpeta)
    
    def toggle_compresion(self, tipo):
        if tipo == "portada":
            if self.compresion_jpeg_portada.get():
                self.spin_calidad_portada.config(state=tk.NORMAL)
            else:
                self.spin_calidad_portada.config(state=tk.DISABLED)
        else:
            if self.compresion_jpeg_contraportada.get():
                self.spin_calidad_contraportada.config(state=tk.NORMAL)
            else:
                self.spin_calidad_contraportada.config(state=tk.DISABLED)
    
    def seleccionar_internas(self, opcion):
        if opcion == "CCITT Group 4":
            messagebox.showwarning("Aviso", "Las imágenes internas se convertirán a blanco y negro")
    
    def actualizar_progreso(self, valor, texto=None):
        if texto:
            self.progress_label.config(text=texto)
        self.progress_bar['value'] = valor
        self.root.update_idletasks()
    
    def iniciar_procesamiento(self):
        carpeta_raiz = self.entry_carpeta.get()
        if not carpeta_raiz or not os.path.isdir(carpeta_raiz):
            messagebox.showerror("Error", "Seleccione una carpeta válida")
            return

        try:
            config = {
                'dpi_portadas': int(self.spin_dpi_portada.get()),
                'dpi_contraportadas': int(self.spin_dpi_contraportada.get()),
                'dpi_internas': int(self.spin_dpi_portada.get()),
                'formato_internas': self.opcion_internas.get(),
                'calidad_jpeg_portada': int(self.spin_calidad_portada.get()) if self.compresion_jpeg_portada.get() else None,
                'calidad_jpeg_contraportada': int(self.spin_calidad_contraportada.get()) if self.compresion_jpeg_contraportada.get() else None
            }

            # Validar DPI
            for dpi in [config['dpi_portadas'], config['dpi_contraportadas'], config['dpi_internas']]:
                if not 150 <= dpi <= 1200:
                    raise ValueError("Los valores de DPI deben estar entre 150 y 1200")

            total_carpetas = sum(1 for name in os.listdir(carpeta_raiz) 
                            if os.path.isdir(os.path.join(carpeta_raiz, name)))
            procesadas = 0
            imagenes_totales = 0

            for folder_name in os.listdir(carpeta_raiz):
                folder_path = os.path.join(carpeta_raiz, folder_name)
                if os.path.isdir(folder_path):
                    input_folder = os.path.join(folder_path, 'input')
                    output_folder = os.path.join(folder_path, 'output')
                    
                    if os.path.exists(input_folder):
                        if not os.path.exists(output_folder):
                            os.makedirs(output_folder)
                        
                        self.actualizar_progreso(
                            (procesadas/total_carpetas)*100, 
                            f"Procesando {folder_name}..."
                        )
                        
                        imagenes = process_images(input_folder, output_folder, config)
                        pdf_path = os.path.join(output_folder, "documento.pdf")
                        
                        if generar_pdf(imagenes, pdf_path):
                            imagenes_totales += len(imagenes)
                            procesadas += 1

            self.actualizar_progreso(100, "Procesamiento completado")
            messagebox.showinfo(
                "Resultado",
                f"Procesadas {procesadas} carpetas\n"
                f"Total imágenes convertidas: {imagenes_totales}"
            )
        
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error:\n{str(e)}")
            self.actualizar_progreso(0, "Error en el procesamiento")

# ------------------------- EJECUCIÓN -------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorPDFApp(root)
    root.mainloop()