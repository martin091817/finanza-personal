from datetime import datetime
from flask import Blueprint, request, jsonify
from .models import Ingreso, Gasto, Ahorro
from . import db

main = Blueprint('main', __name__)

# Registro de ingresos

@main.route('/ingresos', methods=['POST'])
def create_ingreso():
    data = request.get_json()

    # Convertir el string de fecha a un objeto datetime.date
    fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()

    new_ingreso = Ingreso(
        fecha=fecha,
        concepto=data['concepto'],
        valor=data['valor'],
        tipo=data['tipo'],
        metodo=data['metodo'],
        usuario_id=data['usuario_id']
    )
    db.session.add(new_ingreso)
    db.session.commit()
    return jsonify({'message': 'Ingreso created successfully'}), 201

# Crear gasto

@main.route('/gastos', methods=['POST'])
def create_gasto():
    data = request.get_json()
    fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    new_gasto = Gasto(
        fecha=fecha,
        concepto=data['concepto'],
        valor=data['valor'],
        tipo=data['tipo'],
        metodo=data['metodo'],
        usuario_id=data['usuario_id']
    )
    db.session.add(new_gasto)
    db.session.commit()
    return jsonify({'message': 'Gasto created successfully'}), 201

# Obtener gastos

@main.route('/gastos', methods=['GET'])
def get_gastos():
    gastos = Gasto.query.all()
    result = [{'id': g.id, 'fecha': g.fecha, 'concepto': g.concepto, 'valor': g.valor, 'tipo': g.tipo, 'metodo': g.metodo, 'usuario_id': g.usuario_id} for g in gastos]
    return jsonify(result), 200

# Actualizar Gasto

@main.route('/gastos/<int:gasto_id>', methods=['PUT'])
def update_gasto(gasto_id):
    data = request.get_json()
    gasto = Gasto.query.get_or_404(gasto_id)
    gasto.fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    gasto.concepto = data['concepto']
    gasto.valor = data['valor']
    gasto.tipo = data['tipo']
    gasto.metodo = data['metodo']
    db.session.commit()
    return jsonify({'message': 'Gasto updated successfully'}), 200

# Eliminar un gasto

@main.route('/gastos/<int:gasto_id>', methods=['DELETE'])
def delete_gasto(gasto_id):
    gasto = Gasto.query.get_or_404(gasto_id)
    db.session.delete(gasto)
    db.session.commit()
    return jsonify({'message': 'Gasto deleted successfully'}), 200

# Crear Ahorro

@main.route('/ahorros', methods=['POST'])
def create_ahorro():
    data = request.get_json()
    fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    new_ahorro = Ahorro(
        fecha=fecha,
        concepto=data['concepto'],
        valor=data['valor'],
        tipo=data['tipo'],
        metodo=data['metodo'],
        usuario_id=data['usuario_id']
    )
    db.session.add(new_ahorro)
    db.session.commit()
    return jsonify({'message': 'Ahorro created successfully'}), 201

# Obtener Todos los Ahorros

@main.route('/ahorros', methods=['GET'])
def get_ahorros():
    ahorros = Ahorro.query.all()
    result = [{'id': a.id, 'fecha': a.fecha, 'concepto': a.concepto, 'valor': a.valor, 'tipo': a.tipo, 'metodo': a.metodo, 'usuario_id': a.usuario_id} for a in ahorros]
    return jsonify(result), 200

# Actualizar un ahorro

@main.route('/ahorros/<int:ahorro_id>', methods=['PUT'])
def update_ahorro(ahorro_id):
    data = request.get_json()
    ahorro = Ahorro.query.get_or_404(ahorro_id)
    ahorro.fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    ahorro.concepto = data['concepto']
    ahorro.valor = data['valor']
    ahorro.tipo = data['tipo']
    ahorro.metodo = data['metodo']
    db.session.commit()
    return jsonify({'message': 'Ahorro updated successfully'}), 200

#Eliminar un ahorro

@main.route('/ahorros/<int:ahorro_id>', methods=['DELETE'])
def delete_ahorro(ahorro_id):
    ahorro = Ahorro.query.get_or_404(ahorro_id)
    db.session.delete(ahorro)
    db.session.commit()
    return jsonify({'message': 'Ahorro deleted successfully'}), 200
