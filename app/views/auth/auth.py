from flask import request
from flask_restx import Resource, Namespace

from app.container import user_service
from app.auth import generate_token, decode_token
from app.exceptions import BadRequest, NotAuthorized

api = Namespace('auth')


@api.route('/login')
class AuthViews(Resource):
    def post(self):
        """
        Authorize a user, returning auth tokens
        """
        email = request.json.get('email')
        password = request.json.get('password')

        if not all([email, password]):
            raise BadRequest('Missing email or password')

        user = user_service.get_by_email(email)
        if user is None:
            raise NotAuthorized('User not found')

        is_correct_password = user_service.compare_passwords(
            password,
            user.password
        )

        if not is_correct_password:
            raise NotAuthorized('Incorrect password')

        user_data = {'email': user.email, 'user_id': user.id}

        access_token = generate_token(user_data)
        refresh_token = generate_token(user_data, refresh=True)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 201

    def put(self):
        refresh_token = request.json.get('refresh_token')
        if not refresh_token:
            raise BadRequest('Missing refresh token')

        user_data = decode_token(refresh_token)
        if user_data is None:
            raise NotAuthorized('Invalid token')

        access_token = generate_token(user_data)
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }


@api.route('/register')
class RegisterView(Resource):
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')

        if not all([email, password]):
            raise BadRequest('Missing email or password')

        if user_service.get_by_email(email):
            raise BadRequest('User already exists')

        user_service.create({'email': email, 'password': password})
        return '', 201
