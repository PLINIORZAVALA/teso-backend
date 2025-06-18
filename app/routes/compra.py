from flask import Blueprint, request, jsonify
import os
from app.models import db, Compra, Usuario, Proveedor
from datetime import datetime

bp = Blueprint(f'compra_{os.getpid()}', __name__)

# Listar todas las compras
@bp.route('/', methods=['GET'])
def listar_compras():
    compra = Compra.query.all()
    return jsonify([{
        'id': c.id,
        'fecha': c.fecha.isoformat(),
        'usuario_id': c.usuario_id,
        'proveedor_id': c.proveedor_id
    } for c in compra])

# Agregar una nueva compra
@bp.route('/', methods=['POST'])
def agregar_compra():
    data = request.json

    # Validar existencia de usuario y proveedor
    usuario = Usuario.query.get(data['usuario_id'])
    proveedor = Proveedor.query.get(data['proveedor_id'])

    if not usuario:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    if not proveedor:
        return jsonify({'error': 'Proveedor no encontrado'}), 404

    nueva_compra = Compra(
        usuario_id=data['usuario_id'],
        proveedor_id=data['proveedor_id'],
        fecha=datetime.utcnow()
    )

    db.session.add(nueva_compra)
    db.session.commit()

    return jsonify({'mensaje': 'Compra registrada correctamente'}), 201
