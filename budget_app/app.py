from flask import Flask
from flask_restful import Api

from flask_migrate import Migrate
from config import Config
from extensions import db

from resources.expense import ExpenseListResource, ExpenseYearFilterResource, ExpenseMonthFilterResource
from resources.user import UserResource, UserListResource


def create_app() -> Flask:
    """Function create an Flask application and return it."""
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_resources(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    """Function register all resources within application and share endpoints for specify resource."""
    api = Api(app)
    api.add_resource(ExpenseListResource, '/expenses')
    api.add_resource(ExpenseYearFilterResource, '/expenses/<int:year>')
    api.add_resource(ExpenseMonthFilterResource, '/expenses/<int:year>/<int:month>')
    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<string:username>')


if __name__ == '__main__':
    app = create_app()
    app.run()