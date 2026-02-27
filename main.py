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

        self.title("Termux Hub & Hack Launcher")
        self.geometry("600x700")
        self.counter = 0
        self.tools_path = "/data/data/com.termux/files/home/AllHackingTools"

        # Título
        self.label = ctk.CTkLabel(self, text="🛡️ Termux Ultimate Hub", font=ctk.CTkFont(size=26, weight="bold"))
        self.label.pack(padx=20, pady=(20, 10), fill="x")

        # --- SECCIÓN DE HERRAMIENTAS (HACKING) ---
        self.hack_frame = ctk.CTkFrame(self, border_width=2, border_color="#e74c3c")
        self.hack_frame.pack(padx=20, pady=10, fill="x")
        
        self.hack_label = ctk.CTkLabel(self.hack_frame, text="Lanzador de AllHackingTools", font=ctk.CTkFont(size=16, weight="bold"))
        self.hack_label.pack(pady=10)

        # Obtener lista de carpetas en AllHackingTools
        self.tools_list = self.get_tools()
        
        self.tool_selector = ctk.CTkOptionMenu(self.hack_frame, values=self.tools_list, fg_color="#c0392b", button_color="#a93226")
        self.tool_selector.pack(pady=10, padx=20, fill="x")
        self.tool_selector.set("Selecciona una herramienta")

        self.btn_launch = ctk.CTkButton(self.hack_frame, text="🚀 Ejecutar Herramienta", command=self.launch_tool, 
                                       fg_color="#e74c3c", hover_color="#c0392b")
        self.btn_launch.pack(pady=10)

        # --- SECCIÓN DE PROGRESO ---
        self.counter_frame = ctk.CTkFrame(self)
        self.counter_frame.pack(padx=20, pady=10, fill="x")
        
        self.progressbar = ctk.CTkProgressBar(self.counter_frame)
        self.progressbar.pack(padx=20, pady=15, fill="x")
        self.progressbar.set(0)

        self.btn_counter = ctk.CTkButton(self.counter_frame, text="Incrementar Meta", command=self.increment_progress)
        self.btn_counter.pack(pady=10)

        # --- SECCIÓN DE NOTAS ---
        self.notes_label = ctk.CTkLabel(self, text="Bloc de Notas de Misión:", font=ctk.CTkFont(size=14, weight="bold"))
        self.notes_label.pack(padx=20, pady=(10, 5), anchor="w")

        self.textbox = ctk.CTkTextbox(self, height=150)
        self.textbox.pack(padx=20, pady=10, fill="both", expand=True)
        
        if os.path.exists("notas.txt"):
            with open("notas.txt", "r") as f:
                self.textbox.insert("0.0", f.read())

        self.btn_save = ctk.CTkButton(self, text="💾 Guardar Cambios", command=self.save_note)
        self.btn_save.pack(padx=20, pady=20)

    def get_tools(self):
        try:
            # Listar solo directorios que no empiecen con punto
            return [d for d in os.listdir(self.tools_path) 
                    if os.path.isdir(os.path.join(self.tools_path, d)) and not d.startswith('.')]
        except Exception:
            return ["Error al cargar herramientas"]

    def launch_tool(self):
        tool = self.tool_selector.get()
        if tool == "Selecciona una herramienta" or tool == "Error al cargar herramientas":
            messagebox.showwarning("Aviso", "Por favor, selecciona una herramienta válida.")
            return
        
        tool_dir = os.path.join(self.tools_path, tool)
        
        # Intentar ejecutar el archivo principal de la herramienta (Install.sh, MainMenu.py, etc.)
        # Nota: En Termux, para interactuar con la terminal, lo mejor es abrir una nueva sesión.
        # Aquí lanzaremos un comando que intente abrir la herramienta.
        try:
            # Intentamos buscar un ejecutable común
            cmd = f"cd {tool_dir} && (python3 MainMenu.py || python MainMenu.py || bash Install.sh || bash setup.sh || ls)"
            # Ejecutamos en una nueva ventana de terminal si es posible, o mostramos el comando
            messagebox.showinfo("Lanzador", f"Ejecutando {tool} en la terminal de Termux...\nComando: {cmd}")
            # Esto lo ejecuta en el proceso de Termux de fondo
            subprocess.Popen(["termux-open-url", f"https://google.com"]) # Placeholder o acción real
            # Para ejecutar realmente en la terminal visible:
            os.system(f"am startservice --user 0 -a com.termux.service_execute -n com.termux/.app.TermuxService -d {tool_dir}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo iniciar: {str(e)}")

    def increment_progress(self):
        if self.counter < 100:
            self.counter += 10
            self.progressbar.set(self.counter / 100)
        else:
            self.counter = 0
            self.progressbar.set(0)

    def save_note(self):
        with open("notas.txt", "w") as f:
            f.write(self.textbox.get("0.0", "end"))
        messagebox.showinfo("Éxito", "Notas guardadas correctamente.")

if __name__ == "__main__":
    app = App()
    app.mainloop()
