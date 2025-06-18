from flask import Blueprint, request, jsonify
from app.models import db, Inventario, Compra

bp = Blueprint('inventario', __name__, url_prefix='/api/inventario')

# Listar todos los registros de inventario
@bp.route('/', methods=['GET'])
def listar_inventario():
    inventario = Inventario.query.all()
    return jsonify([{
        'id': item.id,
        'producto': item.producto,
        'cantidad': item.cantidad,
        'ubicacion': item.ubicacion,
        'compra_id': item.compra_id
    } for item in inventario])

# Agregar un nuevo producto al inventario
@bp.route('/', methods=['POST'])
def agregar_inventario():
    data = request.json

    # Verificar que la compra exista
    compra = Compra.query.get(data['compra_id'])
    if not compra:
        return jsonify({'error': 'Compra no encontrada'}), 404

    nuevo_item = Inventario(
        producto=data['producto'],
        cantidad=data['cantidad'],
        ubicacion=data.get('ubicacion', ''),
        compra_id=data['compra_id']
    )

    db.session.add(nuevo_item)
    db.session.commit()

    return jsonify({'mensaje': 'Producto registrado en inventario correctamente'}), 201
