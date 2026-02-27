#!/bin/bash
# Matar procesos previos para evitar conflictos
killall termux-x11 python 2>/dev/null

# Configurar variables de entorno para Termux-X11
export DISPLAY=:1
export XDG_RUNTIME_DIR=${TMPDIR}

# Iniciar el servidor Termux-X11 en segundo plano
termux-x11 :1 &
sleep 3 # Esperar a que el servidor arranque

# Ejecutar la aplicación de Python y capturar errores
python ~/my_gui_app/main.py > ~/app_gui.log 2>&1
