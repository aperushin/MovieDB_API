from app.dao.base import BaseDAO
from app.models import Genre, Director, Movie, User
from flask_sqlalchemy import BaseQuery
from werkzeug.exceptions import NotFound


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class DirectorDAO(BaseDAO[Director]):
    __model__ = Genre


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
