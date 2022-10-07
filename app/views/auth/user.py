from app.container import user_service
from flask import request
from flask_restx import Namespace, Resource

from app.tools.security import auth_required
from app.setup.api.models import user
from app.exceptions import BadRequest

api = Namespace('user')


@api.route('/')
class UserViews(Resource):
    """
    Get user data
    """
    @api.response(401, 'Unauthorized')
    @api.marshal_with(user, code=200, description='OK')
    @auth_required
    def get(self, user_data):
        return user_service.get_item(user_data.get('user_id'))

    @api.response(204, 'Success')
    @api.response(400, 'Validation error')
    @api.response(401, 'Unauthorized')
    @auth_required
    def patch(self, user_data):
        """
        Update user information
        """
        user_id = user_data.get('user_id')
        new_user_data = request.json

        user_service.update(user_id, new_user_data)

        return '', 204


@api.route('/password/')
class UserPasswordViews(Resource):
    @api.response(204, 'Success')
    @api.response(401, 'Unauthorized')
    @auth_required
    def put(self, user_data):
        """
        Change user password
        """
        user = user_service.get_item(user_data.get('user_id'))

        old_password = request.json.get('old_password')
        new_password = request.json.get('new_password')

        if not user_service.compare_passwords(old_password, user.password):
            raise BadRequest('Old password is incorrect')

        user_service.update_password(user.id, new_password)

        return '', 204
