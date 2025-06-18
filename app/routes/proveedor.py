from flask import Blueprint, request, jsonify
from app.models import db, Gasto, Compra

bp = Blueprint('gastos', __name__)

# Listar todos los gastos
@bp.route('/', methods=['GET'])
def listar_gastos():
    gastos = Gasto.query.all()
    return jsonify([{
        'id': g.id,
        'descripcion': g.descripcion,
        'monto': g.monto,
        'fecha': g.fecha.isoformat(),
        'compra_id': g.compra_id
    } for g in gastos])

# Registrar un nuevo gasto (requiere compra_id)
@bp.route('/', methods=['POST'])
def agregar_gasto():
    data = request.json

    # Validar que exista la compra asociada
    compra = Compra.query.get(data['compra_id'])
    if not compra:
        return jsonify({'error': 'Compra no encontrada'}), 404

    nuevo = Gasto(
        descripcion=data['descripcion'],
        monto=data['monto'],
        compra_id=data['compra_id']
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'mensaje': 'Gasto registrado correctamente'}), 201
