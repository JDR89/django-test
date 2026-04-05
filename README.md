API de Gestión de Usuarios y Roles

Este proyecto es una API REST desarrollada con Django y Django REST Framework (DRF) como parte de la materia Programación II. Permite la gestión de usuarios vinculados a roles específicos mediante una base de datos SQLite.

🚀 Requisitos previos

Python 3.10 o superior.

Git instalado.

🛠️ Instalación y ejecución

Para levantar este proyecto localmente, sigue estos pasos:

1. Clonar el repositorio o descargar el código.

2. Crear el entorno virtual:

```bash
python -m venv env
```
3. Activar el entorno virtual:

```bash
# En Git Bash:
source env/Scripts/activate
```
4. Instalar las dependencias:

```bash
pip install -r requirements.txt
```
5. Aplicar las migraciones (crear la base de datos):

```bash
python manage.py migrate
```
6. Iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```


📂 Endpoints principales

- Panel de Administración: `http://127.0.0.1:8000/admin/` (Requiere crear un superusuario).

- Listado de Usuarios (API): `http://127.0.0.1:8000/api/users/`

📝 Notas

Este proyecto utiliza SQLite por defecto, por lo que no requiere configuración de servidores de bases de datos externos.