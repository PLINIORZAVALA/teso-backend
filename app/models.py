from app import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(120), unique=True, nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    contraseña = db.Column(db.String(200), nullable=False) 

    compras = db.relationship('Compra', backref='usuario', lazy=True)



class Proveedor(db.Model):
    __tablename__ = 'proveedor'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    contacto = db.Column(db.String(100))
    productos_suministrados = db.Column(db.Text)

    compras = db.relationship('Compra', backref='proveedor', lazy=True)


class Compra(db.Model):
    __tablename__ = 'compra'

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)

    gastos = db.relationship('Gasto', backref='compra', lazy=True)
    inventarios = db.relationship('Inventario', backref='compra', lazy=True)


class Gasto(db.Model):
    __tablename__ = 'gasto'

    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    compra_id = db.Column(db.Integer, db.ForeignKey('compra.id'), nullable=False)


class Inventario(db.Model):
    __tablename__ = 'inventario'

    id = db.Column(db.Integer, primary_key=True)
    producto = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    ubicacion = db.Column(db.String(50))
    compra_id = db.Column(db.Integer, db.ForeignKey('compra.id'), nullable=False)

