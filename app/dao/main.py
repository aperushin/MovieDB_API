from flask_sqlalchemy import BaseQuery
from sqlalchemy.exc import NoResultFound
from werkzeug.exceptions import NotFound

from app.dao.base import BaseDAO
from app.models import Genre, Director, Movie, User, UserMovie


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorDAO(BaseDAO[Director]):
    __model__ = Director


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all(self, page: int = None, status: str = None) -> list[__model__]:
        stmt: BaseQuery = self._db_session.query(self.__model__)

        if status == 'new':
            stmt = stmt.order_by(Movie.year.desc())

        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []

        return stmt.all()


class UserDAO(BaseDAO[User]):
    __model__ = User

    def get_by_email(self, email: str) -> __model__ | None:
        try:
            user = self._db_session.query(User).filter_by(email=email).one()
        except NoResultFound:
            return None
        return user

    def create(self, user: __model__) -> __model__:
        self._db_session.add(user)
        self._db_session.commit()
        return user

    def update(self, uid: int, user_data: dict) -> None:
        self._db_session.query(User).filter_by(id=uid).update(user_data)
        self._db_session.commit()


class UserMovieDAO(BaseDAO[UserMovie]):
    __model__ = UserMovie

    def add(self, user_movie: UserMovie) -> None:
        self._db_session.add(user_movie)
        self._db_session.commit()

    def get_by_user_id(self, uid: int) -> list[__model__]:
        return self._db_session.query(UserMovie).filter_by(user_id=uid).all()

    def get_item(self, user_id: int, movie_id: int) -> __model__:
        return self._db_session.query(UserMovie).filter_by(user_id=user_id, movie_id=movie_id).one()

    def delete(self, user_movie: UserMovie) -> None:
        self._db_session.delete(user_movie)
        self._db_session.commit()
