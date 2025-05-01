FROM python:3.13-alpine

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apk update && apk add --no-cache mysql-client netcat-openbsd


# Copiar el resto de los archivos
COPY . /app

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Establecer variables de entorno
ENV FLASK_APP=run.py

# Exponer el puerto de Flask
EXPOSE 5000

# Ejecutar el script de espera antes de arrancar la app
ENTRYPOINT ["sh", "/app/wait-for-it.sh"]

