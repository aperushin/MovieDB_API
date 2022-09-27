from flask_restx import fields, Model

from app.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссёр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Квентин Тарантино'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=255, example='Batman'),
    'description': fields.String(required=True, max_length=255, example='Описание'),
    'trailer': fields.String(required=True, max_length=255, example='https://www.youtube.com/watch?v=dQw4w9WgXcQ'),
    'year': fields.Integer(required=True, example=1999),
    'rating': fields.Float(required=True, example=6.9),
    'genre_id': fields.Integer(required=True, example=1),
    'director_id': fields.Integer(required=True, example=1)
})
