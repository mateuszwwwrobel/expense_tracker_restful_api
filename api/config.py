from datetime import timedelta


class Config:
    # General
    DEBUG = True
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite://///home/matt/Programming/Expense_Tracker/backend/api/database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # JWT TOKEN
    SECRET_KEY = 'super_secret_key'
    JWT_ERROR_MESSAGE_KEY = 'message'
