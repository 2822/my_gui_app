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
        self.geometry("800x600") # Tamaño inicial razonable
        
        # Sincronizado con el directorio Home de Termux
        self.home_path = "/data/data/com.termux/files/home"
        self.hacking_tools_path = os.path.join(self.home_path, "AllHackingTools")

        # Título
        self.label = ctk.CTkLabel(self, text="🛡️ X11 Integrated Hub", font=ctk.CTkFont(size=26, weight="bold"))
        self.label.pack(padx=20, pady=(40, 20), fill="x")

        # --- SECCIÓN DE HERRAMIENTAS (HACKING) ---
        self.hack_frame = ctk.CTkFrame(self, border_width=2, border_color="#e74c3c")
        self.hack_frame.pack(padx=30, pady=20, fill="x")
        
        self.hack_label = ctk.CTkLabel(self.hack_frame, text="Lanzador de Herramientas (Home Sync)", font=ctk.CTkFont(size=18, weight="bold"))
        self.hack_label.pack(pady=15)

        # Obtener lista de carpetas en Home y AllHackingTools
        self.tools_list = self.get_tools()
        
        self.tool_selector = ctk.CTkOptionMenu(self.hack_frame, values=self.tools_list, fg_color="#c0392b", button_color="#a93226")
        self.tool_selector.pack(pady=15, padx=30, fill="x")
        self.tool_selector.set("Selecciona una herramienta")

        self.btn_launch = ctk.CTkButton(self.hack_frame, text="🚀 Lanzar en Nueva Ventana", command=self.launch_tool, 
                                       fg_color="#e74c3c", hover_color="#c0392b", height=40)
        self.btn_launch.pack(pady=20)

        self.status_label = ctk.CTkLabel(self.hack_frame, text="Estado: Sincronizado con Home", font=ctk.CTkFont(size=12, slant="italic"))
        self.status_label.pack(pady=(0, 15))

        # --- SECCIÓN DE ACCIONES INFERIORES ---
        self.actions_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.actions_frame.pack(padx=30, pady=30, fill="x", side="bottom")
        self.actions_frame.grid_columnconfigure((0, 1), weight=1)

        self.btn_termux = ctk.CTkButton(self.actions_frame, text="📟 Terminal", command=self.open_terminal, 
                                       fg_color="#34495e", hover_color="#2c3e50", height=45)
        self.btn_termux.grid(row=0, column=0, padx=15, pady=5, sticky="ew")

        self.btn_restart = ctk.CTkButton(self.actions_frame, text="🔄 Reiniciar App", command=self.restart_app,
                                        fg_color="#f39c12", hover_color="#e67e22", height=45)
        self.btn_restart.grid(row=0, column=1, padx=15, pady=5, sticky="ew")

        # Selector de Tema (Opcional)
        self.appearance_mode_menu = ctk.CTkOptionMenu(self, values=["Dark", "Light", "System"],
                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_menu.pack(pady=10, side="bottom")

    def get_tools(self):
        tools = []
        try:
            # Escanear Home (excluyendo carpetas ocultas y la propia app)
            home_tools = [d for d in os.listdir(self.home_path) 
                         if os.path.isdir(os.path.join(self.home_path, d)) 
                         and not d.startswith('.') 
                         and d not in ["my_gui_app", "storage"]]
            tools.extend(home_tools)
            
            # Escanear AllHackingTools si existe
            if os.path.exists(self.hacking_tools_path):
                hacking_tools = [f"AHT/{d}" for d in os.listdir(self.hacking_tools_path) 
                                if os.path.isdir(os.path.join(self.hacking_tools_path, d)) 
                                and not d.startswith('.')]
                tools.extend(hacking_tools)
                
            return sorted(tools)
        except Exception:
            return ["Error al sincronizar Home"]

    def detect_executable(self, tool_dir):
        files = os.listdir(tool_dir)
        # Prioridad de archivos ejecutables
        for f in ["main.py", "MainMenu.py", "start.py", "run.py", "app.py"]:
            if f in files: return f"python3 {f}"
        for f in ["install.sh", "setup.sh", "start.sh", "run.sh", "Install.sh"]:
            if f in files: return f"bash {f}"
        # Cualquier .py o .sh
        for f in files:
            if f.endswith(".py"): return f"python3 {f}"
            if f.endswith(".sh"): return f"bash {f}"
        return ""

    def launch_tool(self):
        tool_selection = self.tool_selector.get()
        if tool_selection == "Selecciona una herramienta":
            return
        
        # Determinar la ruta real (si es de AllHackingTools o de Home)
        if tool_selection.startswith("AHT/"):
            tool_name = tool_selection.replace("AHT/", "")
            tool_dir = os.path.join(self.hacking_tools_path, tool_name)
        else:
            tool_dir = os.path.join(self.home_path, tool_selection)
        
        exec_cmd = self.detect_executable(tool_dir)
        
        if not exec_cmd:
            exec_cmd = "bash" # Fallback a terminal si no se detecta nada

        self.status_label.configure(text=f"Abriendo: {tool_selection}...", text_color="#2ecc71")
        
        # Ejecutamos en una nueva ventana de aterm dentro de X11
        command = f"cd {tool_dir} && chmod +x {exec_cmd.split()[-1]} && {exec_cmd}; exec bash"
        subprocess.Popen(["aterm", "-e", "bash", "-c", command])

    def open_terminal(self):
        # Abre una terminal aterm local en X11
        subprocess.Popen(["aterm", "-e", "bash"])

    def restart_app(self):
        os.system("pkill -f python && bash /data/data/com.termux/files/home/my_gui_app/start_app.sh &")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()
