#!/bin/bash

# 1. Limpieza de procesos anteriores
echo "🧹 Limpiando procesos antiguos..."
pkill -f termux-x11
pkill -f python
rm -rf /tmp/.X11-unix/X1 2>/dev/null

# 2. Configurar Entorno
export DISPLAY=:1
export XDG_RUNTIME_DIR=${TMPDIR}
export PYTHONPATH=$PYTHONPATH:/data/data/com.termux/files/home/my_gui_app

# 3. Intentar abrir la App Android Termux-X11
echo "📱 Abriendo Termux-X11 en Android..."
am start -n com.termux.x11/com.termux.x11.MainActivity > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "⚠️ No se pudo abrir automáticamente la app. Por favor, ábrela manualmente."
fi

# 4. Iniciar el servidor X11 (Backend)
echo "🚀 Iniciando servidor X11..."
termux-x11 :1 &
PID_X11=$!
sleep 4 # Esperar a que el servidor arranque

# 5. Ejecutar la aplicación Python
echo "🐍 Ejecutando aplicación Python..."
cd /data/data/com.termux/files/home/my_gui_app
python3 main.py > app_debug.log 2>&1 &
PID_PY=$!

echo "✅ Todo listo. PID X11: $PID_X11, PID App: $PID_PY"
echo "Si la pantalla está negra, cambia a la app Termux-X11."
