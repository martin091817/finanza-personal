from flask import Blueprint, request, jsonify
from .models import Usuario
from . import db, bcrypt
from flask_jwt_extended import create_access_token  # Importar JWT

auth = Blueprint('auth', __name__)

# Ruta para registrar un nuevo usuario
@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = Usuario(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

# Ruta para iniciar sesión (Login) y obtener un token JWT
@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = Usuario.query.filter_by(username=data['username']).first()

    # Verificar si el usuario existe y la contraseña es correcta
    if user and bcrypt.check_password_hash(user.password, data['password']):
        # Crear un token JWT para el usuario autenticado
        access_token = create_access_token(identity=user.id)
        return jsonify({'token': access_token}), 200  # Devolver el token
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
