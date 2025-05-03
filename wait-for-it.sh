#!/bin/sh

HOST="db"
PORT="3306"
RESOLVE_TIMEOUT=30  # Tiempo máximo para intentar resolver el nombre en segundos
RESOLVE_INTERVAL=2   # Intervalo entre intentos de resolución en segundos
RESOLVE_ATTEMPTS=$((RESOLVE_TIMEOUT / RESOLVE_INTERVAL))
RESOLVE_COUNT=0

echo "⏳ Intentando resolver el host '$HOST'..."

while [ "$RESOLVE_COUNT" -lt "$RESOLVE_ATTEMPTS" ]; do
  if getent hosts "$HOST" > /dev/null; then
    echo "✅ Host '$HOST' resuelto."
    break
  else
    RESOLVE_COUNT=$((RESOLVE_COUNT + 1))
    echo "❌ No se pudo resolver '$HOST' (intento $RESOLVE_COUNT de $RESOLVE_ATTEMPTS). Esperando $RESOLVE_INTERVAL segundos..."
    sleep "$RESOLVE_INTERVAL"
  fi
done

if [ "$RESOLVE_COUNT" -eq "$RESOLVE_ATTEMPTS" ]; then
  echo "❌ Falló la resolución del host '$HOST' después de $RESOLVE_ATTEMPTS intentos. Saliendo."
  exit 1
fi

echo "⏳ Esperando a que MySQL esté listo en el host '$HOST'..."

# Esperar hasta que el puerto 3306 esté disponible en el contenedor de MySQL
while ! nc -z "$HOST" "$PORT"; do
  sleep 1
done

echo "✅ MySQL está disponible. Iniciando Flask..."
exec python run.py