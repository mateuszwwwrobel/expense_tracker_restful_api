from flask import Flask
from flask_restful import Api

from flask_migrate import Migrate
from config import Config
from extensions import db, jwt

from resources.expense import ExpenseListResource, ExpenseResource, \
    ExpenseYearFilterResource, ExpenseMonthFilterResource
from resources.user import UserResource, UserCreateResource
from resources.token import TokenResource


def create_app() -> Flask:
    """Function create an Flask application and return it."""
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    register_resources(app)
    return app


def register_extensions(app):
    db.init_app(app)
    jwt.init_app(app)
    migrate = Migrate(app, db)


def register_resources(app):
    """Function register all resources within application and share endpoints for specify resource."""
    api = Api(app)
    api.add_resource(ExpenseListResource, '/expenses')
    api.add_resource(ExpenseResource, '/expense/<int:id>')
    api.add_resource(ExpenseYearFilterResource, '/expenses/<int:year>')
    api.add_resource(ExpenseMonthFilterResource, '/expenses/<int:year>/<int:month>')
    api.add_resource(UserCreateResource, '/users')
    api.add_resource(UserResource, '/users/<string:username>')
    api.add_resource(TokenResource, '/token')


if __name__ == '__main__':
    app = create_app()
    app.run()
