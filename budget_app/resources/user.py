from flask_restful import Resource
from flask import request
from http import HTTPStatus
from models.user import User

from utils import hash_password
# from flask_jwt_extended import jwt_required, get_jwt_identity


class UserCreateResource(Resource):

    def post(self):
        data = request.get_json()

        username = data.get('username')
        email = data.get('email')
        non_hash_password = data.get('password')

        if User.get_user_by_username(username):
            return {'message': 'User with that username already exists.'}, HTTPStatus.BAD_REQUEST
        if User.get_user_by_email(email):
            return {'message': 'User with that email already exists.'}, HTTPStatus.BAD_REQUEST

        password = hash_password(non_hash_password)

        user = User(username=username, email=email, password=password)
        user.save()

        return {'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }}, HTTPStatus.CREATED


class UserResource(Resource):
    pass
