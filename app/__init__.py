import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app(config_path):
    app = Flask(__name__)
    CORS(app)

    # Usa ruta absoluta para cargar la configuración
    abs_config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), config_path)
    app.config.from_pyfile(abs_config_path)

    db.init_app(app)

    # Importar rutas y registrar
    from app.routes import gastos, usuarios
    app.register_blueprint(gastos.bp, url_prefix='/api/gastos')
    app.register_blueprint(usuarios.bp, url_prefix='/api/usuarios')

    with app.app_context():
        db.create_all()

    return app
