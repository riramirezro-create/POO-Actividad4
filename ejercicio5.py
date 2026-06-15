import tkinter as tk
from tkinter import messagebox, filedialog
import os


class LectorArchivo:
    """
    Esta clase emula el comportamiento de lectura de archivos
    solicitado en el ejercicio original, adaptado a Python.
    """
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def leer_contenido(self):
        """
        Lee el contenido del archivo de texto. 
        Equivalente a la lectura línea a línea con BufferedReader en Java.
        """
        try:
          
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                return archivo.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo en la ruta:\n{self.ruta_archivo}")
        except Exception as e:
           
            raise Exception(f"No se pudo leer el archivo. Detalle: {e}")

    def leer_en_mayusculas(self):
        """
        Solución al Ejercicio Propuesto 2:
        Lee el contenido y convierte todas las minúsculas a mayúsculas.
        """
        contenido = self.leer_contenido()
        return contenido.upper()



class InterfazLector:
    def __init__(self, root):
        self.root = root
        self.root.title("Lector de Archivos - Ejercicio POO")
        self.root.geometry("600x500")
        self.root.config(padx=20, pady=20)

        
        self.lbl_instruccion = tk.Label(root, text="Ingrese la ruta del archivo de texto o búsquelo:", font=("Arial", 10, "bold"))
        self.lbl_instruccion.pack(pady=(0, 5))

        frame_entrada = tk.Frame(root)
        frame_entrada.pack(fill=tk.X, pady=5)

        
        self.entrada_ruta = tk.Entry(frame_entrada, font=("Arial", 10))
        self.entrada_ruta.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

        
        self.btn_examinar = tk.Button(frame_entrada, text="Examinar...", command=self.buscar_archivo)
        self.btn_examinar.pack(side=tk.RIGHT)

       
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

       
        self.btn_leer_normal = tk.Button(frame_botones, text="Leer Archivo (Original)", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), command=self.mostrar_normal)
        self.btn_leer_normal.pack(side=tk.LEFT, padx=10)

        
        self.btn_leer_mayusculas = tk.Button(frame_botones, text="Leer en Mayúsculas (Propuesto 2)", bg="#2196F3", fg="white", font=("Arial", 10, "bold"), command=self.mostrar_mayusculas)
        self.btn_leer_mayusculas.pack(side=tk.LEFT, padx=10)

        
        self.lbl_resultado = tk.Label(root, text="Contenido del Archivo:", font=("Arial", 10, "bold"))
        self.lbl_resultado.pack(anchor=tk.W, pady=(10, 0))

        
        frame_texto = tk.Frame(root)
        frame_texto.pack(fill=tk.BOTH, expand=True)
        
        self.scrollbar = tk.Scrollbar(frame_texto)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.txt_pantalla = tk.Text(frame_texto, yscrollcommand=self.scrollbar.set, font=("Consolas", 10), bg="#f4f4f4")
        self.txt_pantalla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.txt_pantalla.yview)

    def buscar_archivo(self):
        """Abre un cuadro de diálogo para seleccionar el archivo fácilmente."""
        ruta = filedialog.askopenfilename(title="Seleccionar archivo de texto", filetypes=[("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")])
        if ruta:
            self.entrada_ruta.delete(0, tk.END)
            self.entrada_ruta.insert(0, ruta)

    def ejecutar_lectura(self, a_mayusculas=False):
        """Método auxiliar que conecta la GUI con la lógica de LectorArchivo."""
        ruta = self.entrada_ruta.get().strip()
        
        if not ruta:
            messagebox.showwarning("Atención", "Por favor, ingrese o seleccione la ruta de un archivo.")
            return

        
        lector = LectorArchivo(ruta)
        
        try:
            
            if a_mayusculas:
                contenido = lector.leer_en_mayusculas()
            else:
                contenido = lector.leer_contenido()

         
            self.txt_pantalla.delete(1.0, tk.END)
            self.txt_pantalla.insert(tk.END, contenido)

        except Exception as error:
            
            self.txt_pantalla.delete(1.0, tk.END)
            messagebox.showerror("Error de Lectura", str(error))

    def mostrar_normal(self):
        self.ejecutar_lectura(a_mayusculas=False)

    def mostrar_mayusculas(self):
        self.ejecutar_lectura(a_mayusculas=True)


if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = InterfazLector(ventana_principal)
    ventana_principal.mainloop()
