FROM python:3.13-alpine

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema (incluyendo el cliente MySQL)
RUN apk update && apk add --no-cache mysql-client

# Copiar requerimientos e instalar dependencias Python
COPY . .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Establecer variables de entorno para Flask
ENV FLASK_APP=run.py

# Exponer el puerto 5000
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "run.py"]
