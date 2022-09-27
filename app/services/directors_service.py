from app.dao.base import BaseDAO
from app.exceptions import ItemNotFound
from app.models import Director


class DirectorsService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Director:
        if director := self.dao.get_by_id(pk):
            return director
        raise ItemNotFound(f'Director with pk={pk} does not exist.')

    def get_all(self, page: int = None) -> list[Director]:
        return self.dao.get_all(page=page)
