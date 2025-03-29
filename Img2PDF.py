import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Img2PDF")

# Obtener dimensiones de la pantalla y centrar la ventana
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()
window_width = 650
window_height = 400
position_x = (screen_width // 2) - (window_width // 2)
position_y = (screen_height // 2) - (window_height // 2)
ventana.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

# Crear LabelFrames organizados en una misma fila
frame_portadas = tk.LabelFrame(ventana, text="Portadas", bg="red", padx=10, pady=10, width=200, height=200)
frame_portadas.pack(side="left", fill="both", expand=True, padx=5, pady=5)

frame_internas = tk.LabelFrame(ventana, text="Internas", bg="green", padx=10, pady=10, width=200, height=200)
frame_internas.pack(side="left", fill="both", expand=True, padx=5, pady=5)

frame_contraportadas = tk.LabelFrame(ventana, text="Contraportadas", bg="blue", padx=10, pady=10, width=200, height=200)
frame_contraportadas.pack(side="left", fill="both", expand=True, padx=5, pady=5)

# Ejecutar la ventana
ventana.mainloop()
