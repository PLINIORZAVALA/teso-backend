import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app(config_path):
    app = Flask(__name__)
    CORS(app)

    # Carga la configuración desde el archivo especificado
    abs_config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), config_path)
    app.config.from_pyfile(abs_config_path)

    # Inicializa la base de datos
    db.init_app(app)

    # Importar y registrar blueprints (rutas)
    from app.routes import usuarios, proveedores, compras, gastos, inventario

    app.register_blueprint(usuarios.bp, url_prefix='/api/usuarios')
    app.register_blueprint(proveedores.bp, url_prefix='/api/proveedores')
    app.register_blueprint(compras.bp, url_prefix='/api/compras')
    app.register_blueprint(gastos.bp, url_prefix='/api/gastos')
    app.register_blueprint(inventario.bp, url_prefix='/api/inventario')

    # Crea todas las tablas si no existen
    with app.app_context():
        db.create_all()

    return app
