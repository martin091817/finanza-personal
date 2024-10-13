from datetime import datetime
from flask import Blueprint, request, jsonify
from .models import Ingreso, Gasto, Ahorro
from . import db

main = Blueprint('main', __name__)

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

# Repetir las rutas similares para gastos y ahorros
