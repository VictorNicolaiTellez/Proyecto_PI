FROM python:3.13-alpine

# Instalar dependencias necesarias
RUN apk add --no-cache gcc musl-dev libffi-dev mariadb-dev

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requerimientos e instalar dependencias Python
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de archivos del proyecto
COPY . .

# Establecer variables de entorno para Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Exponer el puerto 5000
EXPOSE 5000

# Ejecutar la aplicación
CMD ["flask", "run"]
