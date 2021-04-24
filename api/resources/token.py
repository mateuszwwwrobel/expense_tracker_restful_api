from flask_restful import Resource
from http import HTTPStatus
from flask import request
from flask_jwt_extended import create_access_token
from utils import check_password
from models.user import User


class TokenResource(Resource):

    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.get_user_by_username(username)

        if not user or not check_password(password, user.password):
            return {'message': 'Wrong username or password.'},  HTTPStatus.UNAUTHORIZED

        access_token = create_access_token(identity=user.id)
        return {'token': access_token}, HTTPStatus.OK
