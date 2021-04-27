from datetime import timedelta
import os

class Config:
    # General
    DEBUG = True
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_PATH')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JWT TOKEN
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_ERROR_MESSAGE_KEY = 'message'
