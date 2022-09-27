from app.dao.base import BaseDAO
from app.exceptions import ItemNotFound
from app.models import Genre


class GenresService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Genre:
        if genre := self.dao.get_by_id(pk):
            return genre
        raise ItemNotFound(f'Genre with pk={pk} does not exist.')

    def get_all(self, page: int = None) -> list[Genre]:
        return self.dao.get_all(page=page)
