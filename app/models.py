from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(2550), nullable=False)
    description = Column(String(25500), nullable=False)
    trailer = Column(String(2550), nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'), nullable=False)
    genre = relationship(Genre)
    director_id = Column(Integer, ForeignKey(f'{Director.__tablename__}.id'), nullable=False)
    director = relationship(Director)


class User(models.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))
    favourite_genre = Column(ForeignKey(f'{Genre.__tablename__}.id'))


class UserMovie(models.Base):
    __tablename__ = 'favorite_movies'

    id = None
    user_id = Column(ForeignKey(f'{User.__tablename__}.id'), primary_key=True)
    movie_id = Column(ForeignKey(f'{Movie.__tablename__}.id'), primary_key=True)
    movie = relationship(Movie)
