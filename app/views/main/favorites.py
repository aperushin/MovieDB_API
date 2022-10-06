from flask_restx import Namespace, Resource

from app.container import favorite_movies_service
from app.auth import auth_required
from app.setup.api.models import movie

api = Namespace('favorites')


@api.route('/movies/')
class FavoriteMoviesView(Resource):
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    @auth_required
    def get(self, user_data):
        user_id = user_data.get('user_id')
        fav_movies = favorite_movies_service.get_by_user_id(user_id)
        return [m.movie for m in fav_movies]


@api.route('/movies/<int:movie_id>/')
class FavoriteMovieViews(Resource):
    @auth_required
    def post(self, movie_id, user_data):
        user_id = user_data.get('user_id')
        favorite_movies_service.add(user_id, movie_id)
        return '', 201

    @auth_required
    def delete(self, movie_id, user_data):
        user_id = user_data.get('user_id')
        favorite_movies_service.delete(user_id, movie_id)
        return '', 204
