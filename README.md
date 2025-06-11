#  TESO Backend – Sistema de Gestión de Inventario para Tesorería

TESO Backend es la API desarrollada en **Flask (Python)** para gestionar los gastos en tesorería institucional. Permite registrar, consultar y visualizar en tiempo real los gastos realizados por los responsables, promoviendo una rendición de cuentas transparente y organizada al final del periodo fiscal.

---

##  Estructura del Proyecto

```bash
inventario-tesoreria/
│
├── app/                             # Lógica principal de la aplicación Flask
│   ├── __init__.py                  # Inicializa la app con configuración dinámica
│   ├── routes/
│   │   ├── __init__.py              # Agrupa rutas
│   │   ├── gastos.py                # Endpoints de gastos
│   │   └── usuarios.py              # Endpoints de usuarios
│   ├── models.py                    # Modelos de base de datos
│   ├── forms.py                     # (Opcional) Formularios Flask-WTF
│   ├── templates/                   # HTML con Jinja2 (si aplica)
│   └── static/                      # CSS, JS e imágenes
│
├── config/                          # Configuraciones separadas por sede
│   ├── config_sede_a.py             # Configuración para BD_sede_A (MySQL puerto 5001)
│   └── config_sede_b.py             # Configuración para BD_sede_B (MySQL puerto 5002)
│
├── instance/                        # Carpeta donde se crean las base de datos
│
├── requirements.txt                 # Dependencias Python
├── run_sede_a.py                    # Ejecuta Flask conectado a BD_sede_A en localhost:5000
├── run_sede_b.py                    # Ejecuta Flask conectado a BD_sede_B en localhost:5001
├── main.py                          # Ejecuta Flask conectando ambas sedes y ambos puertos
├── README.md                        # Documentación del proyecto


````

---

##  Tecnología Utilizada

* **Backend**: Python 3 + Flask + Flask-CORS + Flask-SQLAlchemy
* **Base de Datos**: SQLite (archivo local)
* **Formato de Datos**: JSON
* **Cliente sugerido**: `wget`, Postman o cualquier cliente REST

---

##  Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/inventario-tesoreria.git
cd inventario-tesoreria
```

### 2. Crear entorno virtual y activarlo

```bash
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python run_sede_a.py
python run_sede_b.py
python main.py
```

> La aplicación "a" estará corriendo en `http://localhost:5001/`
> La aplicación "b" estará corriendo en `http://localhost:5002/`

---

##  Prueba de Endpoints – Métodos Disponibles
Este es replicable para `http://localhost:5001/` y `http://localhost:5002/` solo es cambiar la dirección de puerto. Como ejemplo se realiza con `http://localhost:5001/`

### GET: Listar gastos

```bash
wget --method=GET http://localhost:5001/api/gastos/ -O -
```

---

### POST: Agregar nuevo gasto

```bash
wget --method=POST \
     --header="Content-Type: application/json" \
     --body-data='{
       "descripcion": "Compra de útiles",
       "monto": 150.75,
       "responsable": "Carlos Rojas"
     }' \
     http://localhost:5001/api/gastos/ -O -
```

---

###  GET: Listar usuarios

```bash
wget --method=GET http://localhost:5001/api/usuarios/ -O -
```

---

###  POST: Crear nuevo usuario

```bash
wget --method=POST \
     --header="Content-Type: application/json" \
     --body-data='{
       "nombre": "María López",
       "correo": "maria@ejemplo.com",
       "rol": "Tesorera"
     }' \
     http://localhost:5001/api/usuarios/ -O -
```

---

##  Base de Datos

Por defecto, la base de datos es un archivo SQLite llamado `data.db`, generado automáticamente en la raíz del proyecto la primera vez que ejecutas la app.

* Abrir la carpeta donde se encuentran las bases de datos
```bash
cd apiRestSistema-tesoreria/instance/
```

* Luego abrir en sell la base de datos:

```bash
sqlite3 data_sede_a.db
sqlite3 data_sede_b.db
```

* Comandos útiles:

```sql
.tables               -- Muestra las tablas disponibles
.schema gasto         -- Muestra estructura de la tabla `gasto`
SELECT * FROM gasto;  -- Muestra todos los registros de gastos
SELECT * FROM usuario;-- Muestra todos los usuarios registrados
.exit                 -- Salir de SQLite
```

---

## Personalización

Si deseas cambiar la configuración de la base de datos o utilizar otro motor (PostgreSQL, MySQL), modifica la siguiente línea en `app/__init__.py`:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
```

También puedes agregar variables personalizadas en `config.py` o en el directorio `instance/`.

---

## Licencia

Este proyecto está bajo la Licencia MIT. Eres libre de usar, modificar y distribuir con fines educativos o institucionales.

---

