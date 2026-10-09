# Bitácora Dev

Blog web hecho con Django donde se publican apuntes y avances sobre el aprendizaje de Python y Django. Permite registrarse, iniciar sesión y, una vez autenticado, crear, editar y borrar posts con imagen. Cualquier visitante puede leer los posts.

## Tecnologías utilizadas

- Python 3
- Django 5.2
- SQLite (base de datos por defecto de Django)
- Pillow (manejo de imágenes subidas)
- python-dotenv (variables de entorno)
- HTML y CSS propios (sin frameworks de estilos)

## Funcionalidades principales

- Listado y detalle de posts, visibles para cualquier visitante.
- CRUD de posts desde la interfaz web (crear, editar y borrar requieren iniciar sesión).
- Carga y visualización de una imagen por post.
- Registro de usuarios, inicio y cierre de sesión.
- Perfil de usuario con biografía, fecha de nacimiento y avatar.
- Rutas protegidas: quien no inició sesión es redirigido al login.
- Panel de administración de Django con los modelos `Posteo` y `Perfil`.
- Tests automáticos de autenticación y del CRUD de posts.

## Instalación

### 1. Clonar el repositorio

```bash
git clone <URL-DE-ESTE-REPOSITORIO>
cd <carpeta-del-repositorio>
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
```

Activarlo en Windows (PowerShell):

```powershell
venv\Scripts\Activate.ps1
```

Activarlo en Windows (CMD):

```cmd
venv\Scripts\activate.bat
```

Activarlo en macOS / Linux:

```bash
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

Copiá el archivo de ejemplo y completá los valores:

```bash
cp .env.example .env        # en Windows: copy .env.example .env
```

| Variable     | Descripción                                          |
|--------------|------------------------------------------------------|
| `SECRET_KEY` | Clave secreta de Django (generá una propia).         |
| `DEBUG`      | `True` para desarrollo local, `False` en producción. |

Para generar una `SECRET_KEY`:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

> Si no creás el archivo `.env`, el proyecto arranca igual con una clave de desarrollo, pero solo debe usarse de forma local.

### 5. Crear la base de datos (migraciones)

```bash
python manage.py migrate
```

Opcional: cargar tres posts de ejemplo.

```bash
python manage.py loaddata posteos
```

### 6. Iniciar el servidor

```bash
python manage.py runserver
```

Abrí <http://127.0.0.1:8000/> en el navegador.

### 7. Crear un superusuario (para probar el panel de administración)

```bash
python manage.py createsuperuser
```

Después ingresá a <http://127.0.0.1:8000/admin/>.

## Probar el proyecto desde cero

El repositorio no incluye `db.sqlite3` ni la carpeta `media/`; se generan solos:

1. `python manage.py migrate` crea `db.sqlite3`.
2. La carpeta `media/` se crea cuando se sube la primera imagen (de un post o de un avatar).
3. Para ver el flujo completo: registrarse en `/usuarios/registro/`, iniciar sesión, crear un post con imagen en `/posts/crear/` y comprobar que se ve en el detalle.

## Rutas principales

| Ruta                         | Descripción                | ¿Requiere sesión? |
|------------------------------|----------------------------|-------------------|
| `/`                          | Inicio con los últimos posts | No              |
| `/posts/`                    | Listado de posts           | No                |
| `/posts/<id>/`               | Detalle de un post         | No                |
| `/posts/crear/`              | Crear post                 | Sí                |
| `/posts/<id>/editar/`        | Editar post                | Sí                |
| `/posts/<id>/borrar/`        | Borrar post                | Sí                |
| `/usuarios/registro/`        | Registro                   | No                |
| `/usuarios/iniciar-sesion/`  | Inicio de sesión           | No                |
| `/usuarios/perfil/`          | Perfil del usuario         | Sí                |
| `/usuarios/perfil/editar/`   | Editar perfil              | Sí                |
| `/admin/`                    | Panel de administración    | Superusuario      |

## Ejecutar los tests

```bash
python manage.py test
```

## Estructura del proyecto

```
mi_blog/     Configuración del proyecto (settings, urls)
posts/       App del blog: modelo Posteo, vistas, formularios, templates y estáticos
usuarios/    App de usuarios: registro, login, logout y perfil
templates/   Plantilla base compartida
```

## Autor

Tomás Cascallares — proyecto final del curso de Desarrollo Full Stack (Coderhouse).
