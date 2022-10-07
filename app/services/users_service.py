from app.dao.main import UserDAO
from app.exceptions import ItemNotFound
from app.models import User
from app.tools.security import generate_hash


class UsersService:

    UPDATEBLE_FIELDS = {'name', 'surname', 'favourite_genre'}

    def __init__(self, dao: UserDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} does not exist.')

    def get_all(self, page: int = None) -> list[User]:
        return self.dao.get_all(page=page)

    def get_by_email(self, email: str) -> User:
        return self.dao.get_by_email(email)

    def create(self, user_data: dict) -> User:
        user_data['password'] = generate_hash(user_data['password'])
        new_user = User(**user_data)
        user_added = self.dao.create(new_user)
        return user_added

    def update(self, uid: int, user_data: dict) -> None:
        filtered_data = {k: v for k, v in user_data.items() if k in self.UPDATEBLE_FIELDS}
        self.dao.update(uid, filtered_data)

    def update_password(self, uid: int, password: str) -> None:
        new_password = generate_hash(password)
        self.dao.update(uid, {'password': new_password})
