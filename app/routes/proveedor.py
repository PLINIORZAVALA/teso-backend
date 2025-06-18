from flask import Blueprint, request, jsonify
from app.models import db, Proveedor

bp = Blueprint('proveedor', __name__, url_prefix='/api/proveedor')

# Listar todos los proveedores
@bp.route('/', methods=['GET'])
def listar_proveedores():
    proveedor = Proveedor.query.all()
    return jsonify([{
        'id': p.id,
        'nombre': p.nombre,
        'contacto': p.contacto,
        'productos_suministrados': p.productos_suministrados
    } for p in proveedor])

# Agregar un nuevo proveedor
@bp.route('/', methods=['POST'])
def agregar_proveedor():
    data = request.json

    nuevo_proveedor = Proveedor(
        nombre=data['nombre'],
        contacto=data.get('contacto'),
        productos_suministrados=data.get('productos_suministrados', '')
    )

    db.session.add(nuevo_proveedor)
    db.session.commit()

    return jsonify({'mensaje': 'Proveedor registrado correctamente'}), 201
