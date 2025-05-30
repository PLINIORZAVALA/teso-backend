from flask import Blueprint, request, jsonify
from app.models import db, Usuario

bp = Blueprint('usuarios', __name__)

@bp.route('/', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([{
        'id': u.id,
        'nombre': u.nombre,
        'correo': u.correo,
        'rol': u.rol
    } for u in usuarios])

@bp.route('/', methods=['POST'])
def crear_usuario():
    data = request.json
    nuevo = Usuario(
        nombre=data['nombre'],
        correo=data['correo'],
        rol=data['rol']
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario creado'}), 201
