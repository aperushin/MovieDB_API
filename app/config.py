import base64
import os
from pathlib import Path
from typing import Type

BASE_DIR = Path(__file__).resolve().parent.parent


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', '&Ph1n9z00V1w')
    JSON_AS_ASCII = False

    ITEMS_PER_PAGE = 12

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 130

    PWD_HASH_SALT = b'xx8peF35dQvn9nuTgF'
    PWD_HASH_ITERATIONS = 100_000
    HASH_ALGORYTHM = 'sha256'
    JWT_ALGORYTHM = 'HS256'

    RESTX_JSON = {
        'ensure_ascii': False,
    }


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    # SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR.joinpath('app.db').as_posix()
    SQLALCHEMY_DATABASE_URI = "postgresql://test:12345@db:5432"


class ProductionConfig(BaseConfig):
    DEBUG = False
    # TODO: дополнить конфиг


class ConfigFactory:
    flask_env = os.getenv('FLASK_ENV')

    @classmethod
    def get_config(cls) -> Type[BaseConfig]:
        # if cls.flask_env == 'development':
        #     return DevelopmentConfig
        # elif cls.flask_env == 'production':
        #     return ProductionConfig
        # elif cls.flask_env == 'testing':
        #     return TestingConfig
        # raise NotImplementedError
        return DevelopmentConfig


config = ConfigFactory.get_config()
