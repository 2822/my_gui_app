import customtkinter as ctk
from tkinter import messagebox
import os

# Configuración de apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Termux Modern Studio")
        self.geometry("500x550")
        self.counter = 0

        # Configuración de cuadrícula (Grid)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)

        # Título
        self.label = ctk.CTkLabel(self, text="🚀 Termux GUI Pro", font=ctk.CTkFont(size=24, weight="bold"))
        self.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="ew")

        # Sección de Contador y Progreso
        self.counter_frame = ctk.CTkFrame(self)
        self.counter_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        self.counter_frame.grid_columnconfigure(0, weight=1)

        self.label_counter = ctk.CTkLabel(self.counter_frame, text=f"Progreso del Contador: {self.counter}%", font=ctk.CTkFont(size=14))
        self.label_counter.grid(row=0, column=0, pady=(10, 5))

        self.progressbar = ctk.CTkProgressBar(self.counter_frame)
        self.progressbar.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.progressbar.set(0)

        self.btn_counter = ctk.CTkButton(self.counter_frame, text="Incrementar +10%", command=self.increment_progress, 
                                        fg_color="#2ecc71", hover_color="#27ae60")
        self.btn_counter.grid(row=2, column=0, pady=10)

        # Sección de Notas
        self.notes_label = ctk.CTkLabel(self, text="Bloc de Notas (Autoguardado):", font=ctk.CTkFont(size=14, weight="bold"))
        self.notes_label.grid(row=3, column=0, padx=20, pady=(10, 5), sticky="w")

        self.textbox = ctk.CTkTextbox(self, width=400, height=150)
        self.textbox.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")
        
        # Cargar nota previa si existe
        if os.path.exists("notas.txt"):
            with open("notas.txt", "r") as f:
                self.textbox.insert("0.0", f.read())

        # Botones de Acción Inferiores
        self.actions_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.actions_frame.grid(row=5, column=0, padx=20, pady=20, sticky="ew")
        self.actions_frame.grid_columnconfigure((0, 1), weight=1)

        self.btn_save = ctk.CTkButton(self.actions_frame, text="Guardar Nota", command=self.save_note)
        self.btn_save.grid(row=0, column=0, padx=10)

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.actions_frame, values=["Dark", "Light", "System"],
                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=0, column=1, padx=10)

    def increment_progress(self):
        if self.counter < 100:
            self.counter += 10
            self.progressbar.set(self.counter / 100)
            self.label_counter.configure(text=f"Progreso del Contador: {self.counter}%")
        else:
            messagebox.showinfo("¡Completado!", "Has llegado al 100%")
            self.counter = 0
            self.progressbar.set(0)
            self.label_counter.configure(text="Progreso del Contador: 0%")

    def save_note(self):
        nota = self.textbox.get("0.0", "end")
        with open("notas.txt", "w") as f:
            f.write(nota)
        messagebox.showinfo("Éxito", "Nota guardada correctamente en notas.txt")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()
