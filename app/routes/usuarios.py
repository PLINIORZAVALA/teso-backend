from flask import Blueprint, request, jsonify
from app import db
from app.models import Usuario

bp = Blueprint('usuarios', __name__)

# Crear un nuevo usuario
@bp.route('/', methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nuevo_usuario = Usuario(
        nombre=data['nombre'],
        correo=data['correo'],
        rol=data['rol']
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario creado con éxito'}), 201

# Obtener todos los usuarios
@bp.route('/', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    resultado = [
        {
            'id': u.id,
            'nombre': u.nombre,
            'correo': u.correo,
            'rol': u.rol
        } for u in usuarios
    ]
    return jsonify(resultado)

# Obtener usuario por ID
@bp.route('/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify({
        'id': usuario.id,
        'nombre': usuario.nombre,
        'correo': usuario.correo,
        'rol': usuario.rol
    })

# Actualizar usuario
@bp.route('/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.get_json()

    usuario.nombre = data.get('nombre', usuario.nombre)
    usuario.correo = data.get('correo', usuario.correo)
    usuario.rol = data.get('rol', usuario.rol)

    db.session.commit()
    return jsonify({'mensaje': 'Usuario actualizado correctamente'})

# Eliminar usuario
@bp.route('/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario eliminado correctamente'})
