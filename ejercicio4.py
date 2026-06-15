import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje, tamano):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.tamano = tamano
        self.programadores = []

    def equipo_completo(self):
        """Determina si el equipo ha alcanzado su tamaño máximo."""
        return len(self.programadores) >= self.tamano

    def validar_texto(self, texto):
        """Valida que el texto cumpla con las reglas estrictas."""
        if len(texto) >= 20:
            raise Exception("La longitud no puede ser igual o superior a 20 caracteres.")
        
        if any(char.isdigit() for char in texto):
            raise Exception("El nombre no puede tener dígitos.")
            
        texto_sin_espacios = texto.replace(" ", "")
        if not texto_sin_espacios.isalpha():
            raise Exception("El campo debe contener solo texto (no se permiten símbolos).")

    def anadir_programador(self, nombre, apellidos):
        """Añade un programador validando las condiciones previas."""
        if self.equipo_completo():
            raise Exception("El equipo ya está completo.")
        
        self.validar_texto(nombre)
        self.validar_texto(apellidos)
        
        nuevo_programador = Programador(nombre, apellidos)
        self.programadores.append(nuevo_programador)




class ValidadorContrasena:
    @staticmethod
    def validar(psw1, psw2):
        if psw1 != psw2:
            raise Exception("Las contraseñas no coinciden.")
        if len(psw1) < 8:
            raise Exception("La contraseña debe tener mínimo 8 caracteres.")
        if " " in psw1:
            raise Exception("La contraseña no debe tener espacios en blanco.")
        if not any(c.isupper() for c in psw1):
            raise Exception("Debe tener por lo menos un carácter en mayúscula.")
        if not any(c.isdigit() for c in psw1):
            raise Exception("Debe tener por lo menos un número.")
        if not any(not c.isalnum() and not c.isspace() for c in psw1):
            raise Exception("Debe tener por lo menos un carácter especial.")
        return True



class AplicacionPOO(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Actividades POO")
        self.geometry("450x650")
        self.equipo = None

        
        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True)

        frame_maraton = ttk.Frame(notebook)
        notebook.add(frame_maraton, text="Maratón Programación")
        self.configurar_pestana_maraton(frame_maraton)

        frame_psw = ttk.Frame(notebook)
        notebook.add(frame_psw, text="Ejercicio Contraseña")
        self.configurar_pestana_contrasena(frame_psw)

    def configurar_pestana_maraton(self, parent):
        
        tk.Label(parent, text="--- Crear Equipo ---", font=("Arial", 11, "bold")).pack(pady=10)
        
        tk.Label(parent, text="Nombre del equipo:").pack()
        self.entry_nom_eq = tk.Entry(parent, width=40)
        self.entry_nom_eq.pack()

        tk.Label(parent, text="Universidad:").pack()
        self.entry_uni = tk.Entry(parent, width=40)
        self.entry_uni.pack()

        tk.Label(parent, text="Lenguaje de programación:").pack()
        self.entry_len = tk.Entry(parent, width=40)
        self.entry_len.pack()

        tk.Label(parent, text="Tamaño del equipo (2 o 3):").pack()
        self.entry_tam = tk.Entry(parent, width=40)
        self.entry_tam.pack()

        self.btn_crear_eq = tk.Button(parent, text="Instanciar Equipo", command=self.crear_equipo, bg="lightgreen")
        self.btn_crear_eq.pack(pady=10)

        tk.Frame(parent, height=2, bd=1, relief=tk.SUNKEN).pack(fill=tk.X, padx=20, pady=5)

       
        tk.Label(parent, text="--- Añadir Integrante ---", font=("Arial", 11, "bold")).pack(pady=5)

        tk.Label(parent, text="Nombre:").pack()
        self.entry_nom_prog = tk.Entry(parent, width=40, state=tk.DISABLED)
        self.entry_nom_prog.pack()

        tk.Label(parent, text="Apellidos:").pack()
        self.entry_ape_prog = tk.Entry(parent, width=40, state=tk.DISABLED)
        self.entry_ape_prog.pack()

        self.btn_anadir_prog = tk.Button(parent, text="Añadir Integrante", command=self.anadir_integrante, state=tk.DISABLED, bg="lightblue")
        self.btn_anadir_prog.pack(pady=10)

        self.lbl_estado = tk.Label(parent, text="Cree un equipo para comenzar...", fg="gray")
        self.lbl_estado.pack(pady=10)

    def crear_equipo(self):
        nom = self.entry_nom_eq.get()
        uni = self.entry_uni.get()
        leng = self.entry_len.get()
        
        try:
            tam = int(self.entry_tam.get())
            if tam < 2 or tam > 3:
                raise ValueError("El tamaño del equipo debe ser mínimo 2 y máximo 3.")
            
           
            self.equipo = EquipoMaratonProgramacion(nom, uni, leng, tam)
            messagebox.showinfo("Éxito", "El equipo ha sido creado correctamente.")
            
            
            for widget in (self.entry_nom_eq, self.entry_uni, self.entry_len, self.entry_tam, self.btn_crear_eq):
                widget.config(state=tk.DISABLED)

            for widget in (self.entry_nom_prog, self.entry_ape_prog, self.btn_anadir_prog):
                widget.config(state=tk.NORMAL)
            
            self.actualizar_estado_equipo()

        except ValueError as e:
            messagebox.showerror("Error de Valor", str(e))

    def anadir_integrante(self):
        nom = self.entry_nom_prog.get()
        ape = self.entry_ape_prog.get()
        
        try:
           
            self.equipo.anadir_programador(nom, ape)
            messagebox.showinfo("Éxito", f"Integrante '{nom}' añadido exitosamente.")
            
            self.entry_nom_prog.delete(0, tk.END)
            self.entry_ape_prog.delete(0, tk.END)
            self.actualizar_estado_equipo()
            
            if self.equipo.equipo_completo():
                self.entry_nom_prog.config(state=tk.DISABLED)
                self.entry_ape_prog.config(state=tk.DISABLED)
                self.btn_anadir_prog.config(state=tk.DISABLED)
                messagebox.showinfo("Equipo Completo", "Se ha alcanzado el límite de integrantes para este equipo.")

        except Exception as e:
            
            messagebox.showerror("Excepción de Validación", f"Exception: {e}")

    def actualizar_estado_equipo(self):
        if self.equipo:
            estado = f"Programadores en el equipo: {len(self.equipo.programadores)} de {self.equipo.tamano}"
            self.lbl_estado.config(text=estado, fg="blue")

    def configurar_pestana_contrasena(self, parent):
        tk.Label(parent, text="--- Validar Contraseña ---", font=("Arial", 11, "bold")).pack(pady=20)
        
        tk.Label(parent, text="Ingrese contraseña:").pack()
        self.entry_psw1 = tk.Entry(parent, show="*", width=30)
        self.entry_psw1.pack()

        tk.Label(parent, text="Confirme contraseña:").pack()
        self.entry_psw2 = tk.Entry(parent, show="*", width=30)
        self.entry_psw2.pack()

        btn_validar = tk.Button(parent, text="Validar Contraseña", command=self.validar_contrasena, bg="lightcoral", fg="white")
        btn_validar.pack(pady=20)

    def validar_contrasena(self):
        p1 = self.entry_psw1.get()
        p2 = self.entry_psw2.get()
        try:
            ValidadorContrasena.validar(p1, p2)
            messagebox.showinfo("Aprobado", "La contraseña cumple con todos los requisitos de seguridad.")
        except Exception as e:
            messagebox.showerror("Excepción de Contraseña", f"Exception: {e}")

if __name__ == "__main__":
    app = AplicacionPOO()
    app.mainloop()
