from app.exceptions import BadRequest, ItemNotFound
from sqlalchemy.exc import IntegrityError, NoResultFound
from app.dao.main import UserMovieDAO
from app.models import UserMovie


class FavoriteMoviesService:
    def __init__(self, dao: UserMovieDAO) -> None:
        self.dao = dao

    def get_by_user_id(self, user_id: int) -> list[UserMovie]:
        return self.dao.get_by_user_id(user_id)

    def add(self, user_id: int, movie_id: int):
        favorite_movie = UserMovie(user_id=user_id, movie_id=movie_id)
        try:
            self.dao.add(favorite_movie)
        except IntegrityError:
            raise BadRequest('Already exists')

    def delete(self, user_id: int, movie_id: int):
        try:
            favorite_movie = self.dao.get_item(user_id=user_id, movie_id=movie_id)
        except NoResultFound:
            raise ItemNotFound('Not found')
        self.dao.delete(favorite_movie)
