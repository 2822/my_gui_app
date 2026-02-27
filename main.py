import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Hola", "¡Has pulsado el botón!")

def increment_counter():
    global counter
    counter += 1
    label_counter.config(text=f"Contador: {counter}")

root = tk.Tk()
root.title("Mi Aplicación Termux")
root.geometry("300x200")

counter = 0

label = tk.Label(root, text="¡Bienvenido a tu App!", font=("Arial", 14))
label.pack(pady=10)

btn_saludo = tk.Button(root, text="Saludar", command=on_button_click)
btn_saludo.pack(pady=5)

label_counter = tk.Label(root, text="Contador: 0")
label_counter.pack(pady=5)

btn_counter = tk.Button(root, text="Incrementar", command=increment_counter)
btn_counter.pack(pady=5)

root.mainloop()
