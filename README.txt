Proyecto PI
README
# 🎵 UnderSounds
Proyecto web musical con base de datos MySQL. Cada integrante trabaja en su propia copia de la base de datos de manera local.
---
## 🚀 Primeros pasos
Antes de ejecutar la aplicación, es necesario importar la base de datos localmente.
### 🔧 Requisitos
- MySQL Server instalado localmente
- MySQL Workbench o acceso a la línea de comandos
- Archivo SQL de respaldo (‘UndersoundBaseDatos.sql`)
- pip (gestor de paquetes de Python)
---

## ⚙️ Instalación
### 1. Clona el repositorio
```bash
git clone url
cd ubicacion-tu-repo
### 2. Crea y activa un entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
### 3. Instala las dependencias
pip install -r requirements.txt

## 📦 Base de Datos
Recomendamos usar estos valores para la creación de la base de datos, en caso de utilizar cualquier otro deberá modificar 
los valores correspondientes en el establecimiento de la conexión en el fichero dbConnection.py para poder realizar la conexión.
- **database_name:** `undersound`
- **user:** `root`
- **password:** `123456ABC`
---

## 🛠️ Cómo crear e importar la base de datos
1. Abrir MySQL Workbench y conectarse a `localhost`.
2. Ejecutar en una nueva pestaña SQL:
  CREATE DATABASE undersounds;
  USE undersounds;
3. Ir a:  Server > Data Import
4. Seleccionar Import from Self-Contained File y cargar el archivo UndersoundBaseDatos.sql. 
Disponible en la carpeta db del proyecto
5. Asegurarse  de marcar la base de datos undersounds como destino.
6. Clic en Start Import para comenzar la carga de datos.

## ▶️ Ejecución de la aplicación
python run.py
#Accedemos a la siguiente dirección para poder visualizar la pagina
http://localhost:5000
