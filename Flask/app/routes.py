import io
import matplotlib.pyplot as plt
from datetime import datetime
from flask import Blueprint, send_file, request, jsonify
from .models import Ingreso, Gasto, Ahorro
from . import db
from flask_jwt_extended import jwt_required, get_jwt_identity  # Importar JWT
from datetime import datetime

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

# Generar reportes de ingresos con filtros

@main.route('/reportes', methods=['GET'])
@jwt_required()  # Proteger la ruta con JWT
def generar_reporte():
    current_user_id = get_jwt_identity()  # Obtener el ID del usuario autenticado

    # Obtener los filtros desde la solicitud
    categoria = request.args.get('categoria')  # Tipo de ingreso o gasto
    metodo = request.args.get('metodo')  # Método de pago
    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')

    # Convertir las fechas de string a objeto datetime (si existen)
    try:
        if fecha_inicio:
            fecha_inicio = datetime.strptime(fecha_inicio.strip(), '%Y-%m-%d').date()
        if fecha_fin:
            fecha_fin = datetime.strptime(fecha_fin.strip(), '%Y-%m-%d').date()
    except ValueError as e:
        return jsonify({"error": f"Formato de fecha incorrecto: {str(e)}"}), 400

    # Filtrar ingresos y gastos por usuario
    ingresos = Ingreso.query.filter_by(usuario_id=current_user_id).all()
    gastos = Gasto.query.filter_by(usuario_id=current_user_id).all()

    # Filtrar por categoría
    if categoria:
        ingresos = [i for i in ingresos if i.tipo == categoria]
        gastos = [g for g in gastos if g.tipo == categoria]

    # Filtrar por método de pago
    if metodo:
        ingresos = [i for i in ingresos if i.metodo == metodo]
        gastos = [g for g in gastos if g.metodo == metodo]

    # Filtrar por rango de fechas
    if fecha_inicio and fecha_fin:
        ingresos = [i for i in ingresos if fecha_inicio <= i.fecha <= fecha_fin]
        gastos = [g for g in gastos if fecha_inicio <= g.fecha <= fecha_fin]

    # Verificar si hay datos
    if not ingresos and not gastos:
        return jsonify({"message": "No se encontraron datos para los filtros aplicados."}), 200

    # Preparar los datos para graficar
    conceptos_ingresos = [i.concepto for i in ingresos]
    valores_ingresos = [i.valor for i in ingresos]

    conceptos_gastos = [g.concepto for g in gastos]
    valores_gastos = [g.valor for g in gastos]

    # Crear la gráfica
    plt.figure(figsize=(10, 6))

    # Gráfico de ingresos
    plt.subplot(1, 2, 1)
    if ingresos:
        plt.bar(conceptos_ingresos, valores_ingresos, color='green')
        plt.title('Ingresos')
        plt.xticks(rotation=45, ha='right')
    else:
        plt.text(0.5, 0.5, 'No hay ingresos', horizontalalignment='center', verticalalignment='center')

    # Gráfico de gastos
    plt.subplot(1, 2, 2)
    if gastos:
        plt.bar(conceptos_gastos, valores_gastos, color='red')
        plt.title('Gastos')
        plt.xticks(rotation=45, ha='right')
    else:
        plt.text(0.5, 0.5, 'No hay gastos', horizontalalignment='center', verticalalignment='center')

    # Guardar el gráfico en memoria y enviarlo como respuesta
    img = io.BytesIO()
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    # Enviar el gráfico como archivo descargable
    return send_file(img, mimetype='image/png', as_attachment=True, download_name='reporte.png')