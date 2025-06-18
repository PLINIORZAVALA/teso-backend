from flask import Blueprint, request, jsonify
from app.models import db, Gasto

bp = Blueprint('compra', __name__, url_prefix='/api/gastos')

# Obtener todos los gastos
@bp.route('/', methods=['GET'])
def listar_gastos():
    gastos = Gasto.query.all()
    return jsonify([
        {
            'id': g.id,
            'descripcion': g.descripcion,
            'monto': g.monto,
            'fecha': g.fecha.isoformat(),
            'compra_id': g.compra_id
        }
        for g in gastos
    ])

# Registrar un nuevo gasto
@bp.route('/', methods=['POST'])
def agregar_gasto():
    data = request.json

    if not all(k in data for k in ('descripcion', 'monto', 'compra_id')):
        return jsonify({'error': 'Faltan campos requeridos'}), 400

    nuevo = Gasto(
        descripcion=data['descripcion'],
        monto=data['monto'],
        compra_id=data['compra_id']
    )

    db.session.add(nuevo)
    db.session.commit()

    return jsonify({'mensaje': 'Gasto registrado correctamente'}), 201
