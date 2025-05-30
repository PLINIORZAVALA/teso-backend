from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)  # Permitir peticiones desde otros orígenes

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # Puedes cambiar a PostgreSQL/MySQL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'clave_secreta'

    db.init_app(app)

    # Importar rutas
    from app.routes import gastos, usuarios
    app.register_blueprint(gastos.bp, url_prefix='/api/gastos')
    app.register_blueprint(usuarios.bp, url_prefix='/api/usuarios')

    with app.app_context():
        db.create_all()

    return app
