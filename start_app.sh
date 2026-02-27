#!/bin/bash

# 1. Limpieza de procesos anteriores
echo "🧹 Limpiando procesos antiguos..."
pkill -f termux-x11
pkill -f python
pkill -f openbox
pkill -f aterm
rm -rf /tmp/.X11-unix/X1 2>/dev/null

# 2. Configurar Entorno
export DISPLAY=:1
export XDG_RUNTIME_DIR=${TMPDIR}
export PYTHONPATH=$PYTHONPATH:/data/data/com.termux/files/home/my_gui_app

# 3. Intentar abrir la App Android Termux-X11
echo "📱 Abriendo Termux-X11 en Android..."
am start -n com.termux.x11/com.termux.x11.MainActivity > /dev/null 2>&1

# 4. Iniciar el servidor X11
echo "🚀 Iniciando servidor X11..."
termux-x11 :1 &
sleep 3

# 5. Iniciar el Gestor de Ventanas (Openbox)
# Esto añade los botones de cerrar, minimizar y maximizar
echo "🪟 Iniciando Gestor de Ventanas (Openbox)..."
openbox &
sleep 2

# 6. Ejecutar la aplicación Python
echo "🐍 Ejecutando aplicación Python..."
cd /data/data/com.termux/files/home/my_gui_app
python3 main.py > app_debug.log 2>&1 &

echo "✅ Sistema iniciado con soporte para ventanas."
