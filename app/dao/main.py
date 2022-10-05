from flask_sqlalchemy import BaseQuery
from sqlalchemy.exc import NoResultFound
from werkzeug.exceptions import NotFound

from app.dao.base import BaseDAO
from app.models import Genre, Director, Movie, User


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorDAO(BaseDAO[Director]):
    __model__ = Director


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all(self, page: int = None, status: str = None) -> list[__model__]:
        stmt: BaseQuery = self._db_session.query(self.__model__)

        if status == 'new':
            stmt = stmt.order_by(Movie.created.desc())

        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []

        return stmt.all()


class UserDAO(BaseDAO[User]):
    __model__ = User

    def get_by_email(self, email: str) -> User | None:
        try:
            user = self._db_session.query(User).filter_by(email=email).one()
        except NoResultFound:
            return None
        return user

    def create(self, user: User):
        self._db_session.add(user)
        self._db_session.commit()
        return user
