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
│   │   ├── compra.py                # Endpoints de compra
│   │   ├── gastos.py                # Endpoints de gastos
│   │   ├── inventario.py            # Endpoints de inventario
│   │   ├── proveedor.py             # Endpoints de proveedor
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
├── replicacion.py                   # Configuración para realizar la replicación (topologia E-M) 
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

---

## Prueba de Endpoints – Métodos Disponibles

> Las pruebas pueden hacerse tanto en `http://localhost:5001/` como en `http://localhost:5002/`, solo cambia el puerto. En este ejemplo se usa `http://localhost:5001/`.

---

### USUARIOS

#### 1. Crear usuario (POST `/api/usuarios/`)

```bash
wget --method=POST \
     --header="Content-Type: application/json" \
     --body-data='{
       "nombre": "María López",
       "correo": "maria@ejemplo.com",
       "rol": "Tesorera",
       "contraseña": "maria123"
     }' \
     http://localhost:5001/api/usuarios/ -O -
```

#### 2. Obtener todos los usuarios (GET `/api/usuarios/`)

```bash
wget http://localhost:5001/api/usuarios/ -O -
```

#### 3. Obtener usuario por ID (GET `/api/usuarios/1`)

```bash
wget http://localhost:5001/api/usuarios/1 -O -
```

#### 4. Actualizar usuario (PUT `/api/usuarios/1`)

```bash
wget --method=PUT \
     --header="Content-Type: application/json" \
     --body-data='{
       "nombre": "María Actualizada",
       "correo": "maria.actualizada@ejemplo.com",
       "rol": "Administrador",
       "contraseña": "nuevaClave456"
     }' \
     http://localhost:5001/api/usuarios/1 -O -
```
#### 5. Login usuario (POST /api/usuarios/login `/api/usuarios/login`)

```bash
wget --method=POST \
     --header="Content-Type: application/json" \
     --body-data='{
       "correo": "maria.actualizada@ejemplo.com",
       "contraseña": "maria123"
     }' \
     http://localhost:5001/api/usuarios/login -O -
```


#### 6. Eliminar usuario (DELETE `/api/usuarios/1`)

```bash
wget --method=DELETE http://localhost:5001/api/usuarios/1 -O -
```
---

### PROVEEDOR

#### 1. Listar todos los proveedores (GET `/api/proveedor/`)

```bash
wget http://localhost:5001/api/proveedor/ -O -
```

#### 2. Agregar un nuevo proveedor (POST `/api/proveedor/`)

```bash
wget --method=POST \
     --header="Content-Type: application/json" \
     --body-data='{
       "nombre": "Suministros Andinos",
       "contacto": "andinos@correo.com",
       "productos_suministrados": "Papelería, equipos de oficina"
     }' \
     http://localhost:5001/api/proveedor/ -O -
```

---

### COMPRA

#### 1. Listar todas las compras (GET `/api/compra/`)

```bash
wget http://localhost:5001/api/compra/ -O -
```

#### 2. Agregar una nueva compra (POST `/api/compra/`)

```bash
wget --method=POST \
     --header="Content-Type: application/json" \
     --body-data='{
       "usuario_id": 1,
       "proveedor_id": 1
     }' \
     http://localhost:5001/api/compra/ -O -
```
---

### INVENTARIO

#### 1. Listar todo el inventario (GET `/api/inventario/`)

```bash
wget http://localhost:5001/api/inventario/ -O -
```

#### 2. Agregar un producto al inventario (POST `/api/inventario/`)

> Asegúrate de que exista una compra con el ID que pongas en `"compra_id"`.

```bash
wget --method=POST \
     --header="Content-Type: application/json" \
     --body-data='{
       "producto": "Laptop Lenovo",
       "cantidad": 10,
       "ubicacion": "Almacén principal",
       "compra_id": 1
     }' \
     http://localhost:5001/api/inventario/ -O -
```

---

### GASTOS

#### 1. Listar todos los gastos (GET `/api/gastos/`)

```bash
wget http://localhost:5001/api/gastos/ -O -
```

#### 2. Registrar un nuevo gasto (POST `/api/gastos/`)

> Asegúrate de que ya exista una `compra_id` válida.
> Ejemplo con `compra_id = 1`.

```bash
wget --method=POST \
     --header="Content-Type: application/json" \
     --body-data='{
       "descripcion": "Compra de dos Laptop",
       "monto": 300,
       "compra_id": 1
     }' \
     http://localhost:5001/api/gastos/ -O -
```

---


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
SELECT * FROM compra;  -- Muestra todos los registros de compra
SELECT * FROM gasto;-- Muestra todos los usuarios gasto
SELECT * FROM inventario;  -- Muestra todos los registros de inventario
SELECT * FROM proveedor;  -- Muestra todos los registros de proveedor
SELECT * FROM usuario;  -- Muestra todos los registros de usuario
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

