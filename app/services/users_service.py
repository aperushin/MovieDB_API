import hmac

from app.dao.main import UserDAO
from app.exceptions import ItemNotFound
from app.models import User
from app.auth import generate_hash


class UsersService:
    def __init__(self, dao: UserDAO) -> None:
        self.dao = dao

    def compare_passwords(self, password: str, password_hash: str):
        other_password_hash = generate_hash(password)
        return hmac.compare_digest(password_hash, other_password_hash)

    def get_item(self, pk: int) -> User:
        if user := self.dao.get_by_id(pk):
            return user
        raise ItemNotFound(f'User with pk={pk} does not exist.')

    def get_all(self, page: int = None) -> list[User]:
        return self.dao.get_all(page=page)

    def get_by_email(self, email: str):
        return self.dao.get_by_email(email)

    def create(self, user_data: dict) -> User:
        user_data['password'] = generate_hash(user_data['password'])
        new_user = User(**user_data)
        user_added = self.dao.create(new_user)
        return user_added
