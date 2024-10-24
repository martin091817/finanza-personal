from datetime import datetime
from flask import Blueprint, request, jsonify
from .models import Ingreso, Gasto, Ahorro
from . import db
from flask_jwt_extended import jwt_required, get_jwt_identity  # Importar JWT

main = Blueprint('main', __name__)

# Registro de ingresos
@main.route('/ingresos', methods=['POST'])
@jwt_required()  # Proteger la ruta con JWT
def create_ingreso():
    current_user_id = get_jwt_identity()  # Obtener el ID del usuario autenticado del token
    data = request.get_json()
    # Convertir el string de fecha a un objeto datetime.date
    fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()

    new_ingreso = Ingreso(
        fecha=fecha,
        concepto=data['concepto'],
        valor=data['valor'],
        tipo=data['tipo'],
        metodo=data['metodo'],
        usuario_id= current_user_id  # Asociar el ingreso al usuario autenticado
    )
    db.session.add(new_ingreso)
    db.session.commit()
    return jsonify({'message': 'Ingreso created successfully'}), 201

# Crear gasto

@main.route('/gastos', methods=['POST'])
@jwt_required()  # Proteger la ruta con JWT
def create_gasto():
    current_user_id = get_jwt_identity()  # Obtener el ID del usuario autenticado del token
    data = request.get_json()
    fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    new_gasto = Gasto(
        fecha=fecha,
        concepto=data['concepto'],
        valor=data['valor'],
        tipo=data['tipo'],
        metodo=data['metodo'],
        usuario_id= current_user_id  # Asociar el ingreso al usuario autenticado
    )
    db.session.add(new_gasto)
    db.session.commit()
    return jsonify({'message': 'Gasto created successfully'}), 201

# Obtener gastos

@main.route('/gastos', methods=['GET'])
@jwt_required()  # Proteger la ruta con JWT
def get_gastos():
    current_user_id = get_jwt_identity()  # Obtener el ID del usuario autenticado
    gastos = Gasto.query.filter_by(usuario_id=current_user_id).all()  # Obtener solo los gastos del usuario
    result = [{'id': g.id, 'fecha': g.fecha, 'concepto': g.concepto, 'valor': g.valor, 'tipo': g.tipo, 'metodo': g.metodo} for g in gastos]
    return jsonify(result), 200

# Actualizar Gasto

@main.route('/gastos/<int:gasto_id>', methods=['PUT'])
@jwt_required()  # Proteger la ruta con JWT
def update_gasto(gasto_id):
    current_user_id = get_jwt_identity()  # Obtener el ID del usuario autenticado
    gasto = Gasto.query.get_or_404(gasto_id)

    # Verificar si el gasto pertenece al usuario autenticado
    if gasto.usuario_id != current_user_id:
        return jsonify({'message': 'Access denied'}), 403

    data = request.get_json()
    gasto.fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    gasto.concepto = data['concepto']
    gasto.valor = data['valor']
    gasto.tipo = data['tipo']
    gasto.metodo = data['metodo']
    db.session.commit()
    return jsonify({'message': 'Gasto updated successfully'}), 200

# Eliminar un gasto

@main.route('/gastos/<int:gasto_id>', methods=['DELETE'])
@jwt_required()  # Proteger la ruta con JWT
def delete_gasto(gasto_id):
    current_user_id = get_jwt_identity()  # Obtener el ID del usuario autenticado
    gasto = Gasto.query.get_or_404(gasto_id)

    # Verificar si el gasto pertenece al usuario autenticado
    if gasto.usuario_id != current_user_id:
        return jsonify({'message': 'Access denied'}), 403

    db.session.delete(gasto)
    db.session.commit()
    return jsonify({'message': 'Gasto deleted successfully'}), 200

# Crear Ahorro

@main.route('/ahorros', methods=['POST'])
@jwt_required()  # Proteger la ruta con JWT
def create_ahorro():
    current_user_id = get_jwt_identity()  # Obtener el ID del usuario autenticado del token
    data = request.get_json()
    fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    new_ahorro = Ahorro(
        fecha=fecha,
        concepto=data['concepto'],
        valor=data['valor'],
        tipo=data['tipo'],
        metodo=data['metodo'],
        usuario_id= current_user_id  # Asociar el ingreso al usuario autenticado
    )
    db.session.add(new_ahorro)
    db.session.commit()
    return jsonify({'message': 'Ahorro created successfully'}), 201

# Obtener Todos los Ahorros

@main.route('/ahorros', methods=['GET'])
@jwt_required()  # Proteger la ruta con JWT
def get_ahorros():
    current_user_id = get_jwt_identity()  # Obtener el ID del usuario autenticado
    ahorros = Ahorro.query.filter_by(usuario_id=current_user_id).all()  # Obtener solo los ahorros del usuario
    result = [{'id': a.id, 'fecha': a.fecha, 'concepto': a.concepto, 'valor': a.valor, 'tipo': a.tipo, 'metodo': a.metodo} for a in ahorros]
    return jsonify(result), 200

# Actualizar un ahorro

@main.route('/ahorros/<int:ahorro_id>', methods=['PUT'])
@jwt_required()  # Proteger la ruta con JWT
def update_ahorro(ahorro_id):
    current_user_id = get_jwt_identity()  # Obtener el ID del usuario autenticado
    ahorro = Ahorro.query.get_or_404(ahorro_id)

    # Verificar si el ahorro pertenece al usuario autenticado
    if ahorro.usuario_id != current_user_id:
        return jsonify({'message': 'Access denied'}), 403

    data = request.get_json()
    ahorro.fecha = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
    ahorro.concepto = data['concepto']
    ahorro.valor = data['valor']
    ahorro.tipo = data['tipo']
    ahorro.metodo = data['metodo']
    db.session.commit()
    return jsonify({'message': 'Ahorro updated successfully'}), 200

#Eliminar un ahorro

@main.route('/ahorros/<int:ahorro_id>', methods=['DELETE'])
@jwt_required()  # Proteger la ruta con JWT
def delete_ahorro(ahorro_id):
    current_user_id = get_jwt_identity()  # Obtener el ID del usuario autenticado
    ahorro = Ahorro.query.get_or_404(ahorro_id)

    # Verificar si el ahorro pertenece al usuario autenticado
    if ahorro.usuario_id != current_user_id:
        return jsonify({'message': 'Access denied'}), 403

    db.session.delete(ahorro)
    db.session.commit()
    return jsonify({'message': 'Ahorro deleted successfully'}), 200
