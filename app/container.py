from app.dao import GenresDAO, DirectorDAO, MovieDAO, UserDAO, UserMovieDAO

from app.services import (
    GenresService,
    DirectorsService,
    MoviesService,
    UsersService,
    FavoriteMoviesService
)
from app.setup.db import db

# DAO
genre_dao = GenresDAO(db.session)
director_dao = DirectorDAO(db.session)
movie_dao = MovieDAO(db.session)
user_dao = UserDAO(db.session)
user_movie_dao = UserMovieDAO(db.session)

# Services
genre_service = GenresService(dao=genre_dao)
director_service = DirectorsService(dao=director_dao)
movie_service = MoviesService(dao=movie_dao)
user_service = UsersService(dao=user_dao)
favorite_movies_service = FavoriteMoviesService(dao=user_movie_dao)
