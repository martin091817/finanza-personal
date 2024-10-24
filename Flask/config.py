import os
from datetime import timedelta  # Importar timedelta para configurar la expiración del token

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Clave secreta para la aplicación Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'aP8s09@#lM!(2e&KZpQdVb2R%uGf'
    
    # Clave secreta para firmar los tokens JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or '2e2d2a4fbb914a49b6ae13d3457c31d45ae7b1c9a2c6a9d0516bb23248d3ec60'
    
    # Configuración de la base de datos SQLite
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "app.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración para que el token expire en 1 hora
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)  # El token expira en 1 hora

