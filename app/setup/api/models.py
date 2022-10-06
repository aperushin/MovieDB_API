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
    'genre': fields.Nested(genre),
    'director_id': fields.Integer(required=True, example=1),
    'director': fields.Nested(director)
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(max_length=100, example='John'),
    'surname': fields.String(max_length=100, example='Smith'),
    'email': fields.String(required=True, max_length=100, example='a@a.com'),
    'favourite_genre': fields.Integer(example=1)
})

user_movie: Model = api.model('Любимые фильмы', {
    'user_id': fields.Integer(required=True, example=1),
    'movie_id': fields.Integer(required=True, example=1),
    'movie': fields.Nested(movie)
})
