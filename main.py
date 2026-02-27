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

        self.title("Termux Fullscreen Launcher")
        
        # Ajustar bordes al tamaño de la pantalla (Pantalla Completa)
        self.attributes("-fullscreen", True)
        
        # Permitir salir de pantalla completa con la tecla Escape (opcional)
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

        self.tools_path = "/data/data/com.termux/files/home/AllHackingTools"

        # Título
        self.label = ctk.CTkLabel(self, text="🛡️ Smart Termux Hub", font=ctk.CTkFont(size=26, weight="bold"))
        self.label.pack(padx=20, pady=(30, 20), fill="x")

        # --- SECCIÓN DE HERRAMIENTAS (HACKING) ---
        self.hack_frame = ctk.CTkFrame(self, border_width=2, border_color="#e74c3c")
        self.hack_frame.pack(padx=20, pady=10, fill="x")
        
        self.hack_label = ctk.CTkLabel(self.hack_frame, text="Lanzador Inteligente de Herramientas", font=ctk.CTkFont(size=16, weight="bold"))
        self.hack_label.pack(pady=10)

        self.tools_list = self.get_tools()
        self.tool_selector = ctk.CTkOptionMenu(self.hack_frame, values=self.tools_list, fg_color="#c0392b", button_color="#a93226")
        self.tool_selector.pack(pady=15, padx=20, fill="x")
        self.tool_selector.set("Selecciona una herramienta")

        self.btn_launch = ctk.CTkButton(self.hack_frame, text="🚀 Lanzamiento Inteligente", command=self.launch_tool, 
                                       fg_color="#e74c3c", hover_color="#c0392b")
        self.btn_launch.pack(pady=15)

        self.status_label = ctk.CTkLabel(self.hack_frame, text="Estado: Esperando selección...", font=ctk.CTkFont(size=12, slant="italic"))
        self.status_label.pack(pady=(0, 15))

        # --- SECCIÓN DE ACCIONES INFERIORES ---
        self.actions_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.actions_frame.pack(padx=20, pady=20, fill="x")
        self.actions_frame.grid_columnconfigure((0, 1), weight=1)

        self.btn_termux = ctk.CTkButton(self.actions_frame, text="📟 Abrir Termux", command=self.open_termux, 
                                       fg_color="#34495e", hover_color="#2c3e50")
        self.btn_termux.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.btn_restart = ctk.CTkButton(self.actions_frame, text="🔄 Reiniciar App", command=self.restart_app,
                                        fg_color="#f39c12", hover_color="#e67e22")
        self.btn_restart.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Selector de Tema
        self.appearance_mode_menu = ctk.CTkOptionMenu(self, values=["Dark", "Light", "System"],
                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_menu.pack(pady=20)

    def get_tools(self):
        try:
            return sorted([d for d in os.listdir(self.tools_path) 
                    if os.path.isdir(os.path.join(self.tools_path, d)) and not d.startswith('.')])
        except Exception:
            return ["Error al cargar herramientas"]

    def detect_executable(self, tool_dir):
        files = os.listdir(tool_dir)
        for f in ["main.py", "MainMenu.py", "start.py", "run.py"]:
            if f in files: return f"python3 {f}"
        for f in ["install.sh", "setup.sh", "start.sh", "run.sh"]:
            if f in files: return f"bash {f}"
        for f in files:
            if f.endswith(".py"): return f"python3 {f}"
            if f.endswith(".sh"): return f"bash {f}"
        return "ls -la"

    def launch_tool(self):
        tool = self.tool_selector.get()
        if tool == "Selecciona una herramienta" or tool == "Error al cargar herramientas":
            messagebox.showwarning("Aviso", "Selecciona una herramienta válida.")
            return
        
        tool_dir = os.path.join(self.tools_path, tool)
        exec_cmd = self.detect_executable(tool_dir)
        self.status_label.configure(text=f"Detectado: {exec_cmd}", text_color="#2ecc71")
        
        full_command = f"chmod +x {os.path.join(tool_dir, exec_cmd.split()[-1])} && cd {tool_dir} && {exec_cmd}"
        try:
            os.system(f"am startservice --user 0 -a com.termux.service_execute -n com.termux/.app.TermuxService -d '{full_command}'")
            messagebox.showinfo("Lanzador", f"Ejecutando {tool} en Termux.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo iniciar: {e}")

    def open_termux(self):
        os.system("am start --user 0 -n com.termux/.app.TermuxActivity")

    def restart_app(self):
        os.system("pkill -f python && bash /data/data/com.termux/files/home/my_gui_app/start_app.sh &")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()
