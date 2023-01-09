import pytest
from unittest.mock import patch

from app.services import UsersService
from app.models import User


class TestUsersService:

    @pytest.fixture
    @patch('app.dao.UserDAO')
    def users_dao_mock(self, dao_mock):
        test_user = User(
            id=1,
            email='test@example.com',
            password='4MJEx+4A07IfzFAe/LC+L5Rt8zNd1tPQqvnoE/qqLt4='
        )
        dao = dao_mock()
        dao.get_by_email.return_value = test_user
        dao.create.return_value = test_user
        dao.update.return_value = None
        return dao

    @pytest.fixture
    def users_service(self, users_dao_mock):
        return UsersService(dao=users_dao_mock)

    # @pytest.fixture
    # def genre(self, db):
    #     obj = User(name="genre")
    #     db.session.add(obj)
    #     db.session.commit()
    #     return obj

    def test_create_user(self, users_service):
        new_user = users_service.create({
            'email': 'test@example.com',
            'password': '12345'
        })
        assert new_user.email == 'test@example.com'
