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
        rol=data['rol'],
        contraseña=data['contraseña']  
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
            # 🔒 Contraseña no se devuelve por seguridad
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
        # 🔒 Contraseña no se devuelve por seguridad
    })

# Actualizar usuario
@bp.route('/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.get_json()

    usuario.nombre = data.get('nombre', usuario.nombre)
    usuario.correo = data.get('correo', usuario.correo)
    usuario.rol = data.get('rol', usuario.rol)
    if 'contraseña' in data:
        usuario.contraseña = data['contraseña']  # ✅ Se permite actualizar

    db.session.commit()
    return jsonify({'mensaje': 'Usuario actualizado correctamente'})

# Eliminar usuario
@bp.route('/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario eliminado correctamente'})

# Login de usuario
@bp.route('/login', methods=['POST'])
def login_usuario():
    data = request.get_json()
    correo = data.get('correo')
    contraseña = data.get('contraseña')

    if not correo or not contraseña:
        return jsonify({'error': 'Correo y contraseña son obligatorios'}), 400

    usuario = Usuario.query.filter_by(correo=correo).first()

    if usuario and usuario.contraseña == contraseña:
        return jsonify({
            'mensaje': 'Login exitoso',
            'usuario': {
                'id': usuario.id,
                'nombre': usuario.nombre,
                'correo': usuario.correo,
                'rol': usuario.rol
            }
        })
    else:
        return jsonify({'error': 'Credenciales incorrectas'}), 401
