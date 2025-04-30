#!/bin/sh
echo "⏳ Esperando a que MySQL esté listo en el host 'db'..."

# Esperar hasta que el puerto 3306 esté disponible en el contenedor de MySQL
while ! nc -z db 3306; do
  sleep 1
done

echo "✅ MySQL está disponible. Iniciando Flask..."
exec python run.py