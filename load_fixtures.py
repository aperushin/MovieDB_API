from contextlib import suppress
from typing import Any, Type

from sqlalchemy.exc import IntegrityError

from app.config import config
from app.models import Genre, Director, Movie
from app.server import create_app
from app.setup.db import db, models
from app.utils import read_json


def load_data(data: list[dict[str, Any]], model: Type[models.Base]) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))


if __name__ == '__main__':
    fixtures: dict[str, list[dict[str, Any]]] = read_json("fixtures.json")

    app = create_app(config)

    with app.app_context():
        load_data(fixtures['genres'], Genre)
        load_data(fixtures['directors'], Director)
        load_data(fixtures['movies'], Movie)

        with suppress(IntegrityError):
            db.session.commit()
