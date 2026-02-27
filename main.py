import customtkinter as ctk
from tkinter import messagebox
import os
import subprocess

# Configuración de apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Termux Clean Hub Pro")
        self.geometry("900x700")
        
        # Rutas
        self.home_path = "/data/data/com.termux/files/home"
        self.hacking_tools_path = os.path.join(self.home_path, "AllHackingTools")

        # --- TÍTULO ---
        self.label = ctk.CTkLabel(self, text="🛡️ Termux Command Center", font=ctk.CTkFont(size=28, weight="bold"))
        self.label.pack(padx=20, pady=(40, 20), fill="x")

        # --- SECCIÓN: MENÚ DE HERRAMIENTAS (HOME) ---
        self.home_label = ctk.CTkLabel(self, text="📂 Explorador de Herramientas (Home)", font=ctk.CTkFont(size=18, weight="bold"))
        self.home_label.pack(pady=(10, 10))

        # Marco con scroll para las herramientas del home
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=800, height=450, label_text="Tus Carpetas en ~/")
        self.scroll_frame.pack(padx=30, pady=10, fill="both", expand=True)

        self.sync_home_menu()

        # --- SECCIÓN DE ACCIONES INFERIORES ---
        self.actions_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.actions_frame.pack(padx=30, pady=20, fill="x", side="bottom")
        self.actions_frame.grid_columnconfigure((0, 1), weight=1)

        self.btn_termux = ctk.CTkButton(self.actions_frame, text="📟 Nueva Terminal", command=self.open_terminal, 
                                       fg_color="#34495e", hover_color="#2c3e50", height=45)
        self.btn_termux.grid(row=0, column=0, padx=15, pady=5, sticky="ew")

        self.btn_restart = ctk.CTkButton(self.actions_frame, text="🔄 Recargar Interfaz", command=self.restart_app,
                                        fg_color="#f39c12", hover_color="#e67e22", height=45)
        self.btn_restart.grid(row=0, column=1, padx=15, pady=5, sticky="ew")

    def sync_home_menu(self):
        # Limpiar botones anteriores si existen
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        try:
            # Obtener carpetas en Home
            folders = sorted([d for d in os.listdir(self.home_path) 
                            if os.path.isdir(os.path.join(self.home_path, d)) 
                            and not d.startswith('.') 
                            and d not in ["my_gui_app", "storage"]])
            
            # Crear un botón por cada carpeta
            for folder in folders:
                btn = ctk.CTkButton(self.scroll_frame, text=f"📁 {folder}", 
                                   command=lambda f=folder: self.launch_from_home(f),
                                   fg_color="#2c3e50", hover_color="#34495e",
                                   anchor="w", height=35)
                btn.pack(padx=10, pady=5, fill="x")
        except Exception as e:
            error_lbl = ctk.CTkLabel(self.scroll_frame, text=f"Error al sincronizar: {e}")
            error_lbl.pack()

    def launch_from_home(self, folder_name):
        tool_dir = os.path.join(self.home_path, folder_name)
        exec_cmd = self.detect_executable(tool_dir)
        
        if not exec_cmd:
            exec_cmd = "bash" # Abrir terminal en la carpeta si no hay ejecutable claro

        # Lanzar en ventana de aterm
        command = f"cd {tool_dir} && {exec_cmd}; exec bash"
        subprocess.Popen(["aterm", "-title", f"Tool: {folder_name}", "-e", "bash", "-c", command])

    def detect_executable(self, tool_dir):
        files = os.listdir(tool_dir)
        for f in ["main.py", "MainMenu.py", "start.py", "run.py"]:
            if f in files: return f"python3 {f}"
        for f in ["install.sh", "setup.sh", "start.sh", "run.sh"]:
            if f in files: return f"bash {f}"
        for f in files:
            if f.endswith(".py"): return f"python3 {f}"
            if f.endswith(".sh"): return f"bash {f}"
        return ""

    def open_terminal(self):
        subprocess.Popen(["aterm", "-e", "bash"])

    def restart_app(self):
        os.system("pkill -f python && bash /data/data/com.termux/files/home/my_gui_app/start_app.sh &")

if __name__ == "__main__":
    app = App()
    app.mainloop()
