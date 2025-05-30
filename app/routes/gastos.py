from flask import Blueprint, request, jsonify
from app.models import db, Gasto

bp = Blueprint('gastos', __name__)

@bp.route('/', methods=['GET'])
def listar_gastos():
    gastos = Gasto.query.all()
    return jsonify([{
        'id': g.id,
        'descripcion': g.descripcion,
        'monto': g.monto,
        'fecha': g.fecha.isoformat(),
        'responsable': g.responsable
    } for g in gastos])

@bp.route('/', methods=['POST'])
def agregar_gasto():
    data = request.json
    nuevo = Gasto(
        descripcion=data['descripcion'],
        monto=data['monto'],
        responsable=data['responsable']
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({'mensaje': 'Gasto registrado correctamente'}), 201
