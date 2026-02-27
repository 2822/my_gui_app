import customtkinter as ctk
from tkinter import messagebox

# Configuración inicial de CustomTkinter
ctk.set_appearance_mode("dark")  # Modos: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Termux Modern UI")
        self.geometry("400x320")
        self.counter = 0

        # Título principal
        self.label = ctk.CTkLabel(self, text="¡Bienvenido a tu App!", font=ctk.CTkFont(size=20, weight="bold"))
        self.label.pack(pady=20)

        # Botón de saludo
        self.btn_saludo = ctk.CTkButton(self, text="Saludar", command=self.on_button_click)
        self.btn_saludo.pack(pady=10)

        # Contador
        self.label_counter = ctk.CTkLabel(self, text=f"Contador: {self.counter}")
        self.label_counter.pack(pady=10)

        # Botón para incrementar
        self.btn_counter = ctk.CTkButton(self, text="Incrementar", command=self.increment_counter, fg_color="green", hover_color="#006400")
        self.btn_counter.pack(pady=10)

        # Selector de Modo (Oscuro/Claro)
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self, values=["Light", "Dark", "System"],
                                                               command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.pack(pady=20)
        self.appearance_mode_optionemenu.set("Dark")

    def on_button_click(self):
        messagebox.showinfo("Hola", "¡Has pulsado el botón moderno!")

    def increment_counter(self):
        self.counter += 1
        self.label_counter.configure(text=f"Contador: {self.counter}")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()
