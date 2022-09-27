from app.dao.main import MovieDAO
from app.exceptions import ItemNotFound
from app.models import Movie


class MoviesService:
    def __init__(self, dao: MovieDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Movie with pk={pk} does not exist.')

    def get_all(self, page: int = None, status: str = None) -> list[Movie]:
        return self.dao.get_all(page=page, status=status)
