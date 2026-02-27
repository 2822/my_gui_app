# My Termux GUI App

Una aplicación simple de interfaz gráfica (GUI) creada en Python con Tkinter, diseñada específicamente para ejecutarse en el entorno de **Termux** utilizando **Termux-X11**.

## Características
- Interfaz gráfica sencilla con Tkinter.
- Script de inicio automatizado (`start_app.sh`).
- Contador interactivo y mensajes de saludo.

## Requisitos en Termux
1. Instalar dependencias:
   ```bash
   pkg update && pkg upgrade
   pkg install x11-repo python python-tkinter termux-x11-nightly
   ```
2. Tener instalada la aplicación [Termux-X11](https://github.com/termux/termux-x11) en Android.

## Cómo ejecutar
1. Abre la aplicación **Termux-X11** en tu Android.
2. Ejecuta el script de inicio:
   ```bash
   chmod +x start_app.sh
   ./start_app.sh
   ```

## Autor
- **2822** - [rules2822@gmail.com](mailto:rules2822@gmail.com)
