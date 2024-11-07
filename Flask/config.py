import os
from datetime import timedelta
from dotenv import load_dotenv

# Cargar las variables de entorno desde .env
load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Clave secreta para la aplicación Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'clave_por_defecto')
    
    # Clave secreta para firmar los tokens JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'clave_jwt_por_defecto')
    
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', f'sqlite:///{os.path.join(BASE_DIR, "app.db")}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de expiración del token JWT
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=int(os.getenv('JWT_EXPIRATION_HOURS', 1)))

