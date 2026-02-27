import customtkinter as ctk
import os
import subprocess

# Configuración de apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Termux Control Panel")
        self.geometry("400x300")
        
        # Configurar cuadrícula para centrar elementos
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # --- TÍTULO ---
        self.label = ctk.CTkLabel(self, text="🛡️ Control Center", font=ctk.CTkFont(size=24, weight="bold"))
        self.label.grid(row=0, column=0, pady=20)

        # --- BOTONES PRINCIPALES ---
        self.btn_terminal = ctk.CTkButton(self, text="📟 Abrir Consola", 
                                         command=self.open_terminal, 
                                         fg_color="#34495e", hover_color="#2c3e50", 
                                         height=50, font=ctk.CTkFont(size=16, weight="bold"))
        self.btn_terminal.grid(row=1, column=0, padx=40, pady=10, sticky="ew")

        self.btn_restart = ctk.CTkButton(self, text="🔄 Reiniciar App", 
                                        command=self.restart_app,
                                        fg_color="#f39c12", hover_color="#e67e22", 
                                        height=50, font=ctk.CTkFont(size=16, weight="bold"))
        self.btn_restart.grid(row=2, column=0, padx=40, pady=10, sticky="ew")

    def open_terminal(self):
        # Abre una terminal aterm local en X11
        subprocess.Popen(["aterm", "-e", "bash"])

    def restart_app(self):
        # Reinicia la aplicación
        os.system("pkill -f python && bash /data/data/com.termux/files/home/my_gui_app/start_app.sh &")

if __name__ == "__main__":
    app = App()
    app.mainloop()
