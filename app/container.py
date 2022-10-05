from app.dao import GenresDAO, DirectorDAO, MovieDAO, UserDAO

from app.services import (
    GenresService,
    DirectorsService,
    MoviesService,
    UsersService
)
from app.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorDAO(db.session)
movie_dao = MovieDAO(db.session)
user_dao = UserDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UsersService(dao=user_dao)
