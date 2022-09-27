from flask_restx import Namespace, Resource

from app.container import movie_service
from app.setup.api.models import movie
from app.setup.api.parsers import page_status_parser

api = Namespace('movies')


@api.route('/')
class MoviesView(Resource):
    @api.expect(page_status_parser)
    @api.marshal_with(movie, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all movies.
        """
        return movie_service.get_all(**page_status_parser.parse_args())


@api.route('/<int:movie_id>/')
class MovieView(Resource):
    @api.response(404, 'Not Found')
    @api.marshal_with(movie, code=200, description='OK')
    def get(self, movie_id: int):
        """
        Get movie by id.
        """
        return movie_service.get_item(movie_id)
