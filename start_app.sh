#!/bin/bash
# Matar procesos previos para evitar conflictos
pkill -f termux-x11
pkill -f python
rm -rf /tmp/.X11-unix/X1 2>/dev/null

# Configurar variables de entorno críticas
export DISPLAY=:1
export XDG_RUNTIME_DIR=${TMPDIR}
export PYTHONPATH=$PYTHONPATH:/data/data/com.termux/files/home/my_gui_app

# Iniciar el servidor Termux-X11 en segundo plano
termux-x11 :1 &
sleep 4 # Tiempo extra para asegurar que el servidor arranque

# Ejecutar la aplicación usando la ruta absoluta completa
cd /data/data/com.termux/files/home/my_gui_app
python3 main.py > app_debug.log 2>&1 &

echo "Servidor y Aplicación iniciados. Abre la app Termux-X11 en tu Android."
