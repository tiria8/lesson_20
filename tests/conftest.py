import pytest

from unittest.mock import MagicMock

from setup_db import db
from dao.model.director import Director
from dao.model.movie import Movie
from dao.model.genre import Genre
from dao.director import DirectorDAO
from dao.movie import MovieDAO
from dao.genre import GenreDAO

@pytest.fixture()
def director_dao():

    director_dao = DirectorDAO(db.session)

    director_1 = Director(id=1, name="Director 1")
    director_2 = Director(id=2, name="Director 2")

    directors = {
        1: director_1,
        2: director_2
    }

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=directors.values())
    director_dao.create = MagicMock(return_value=Director(id=1, name="Director 1"))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao

@pytest.fixture()
def genre_dao():

    genre_dao = GenreDAO(db.session)

    genre_1 = Genre(id=1, name="Genre 1")
    genre_2 = Genre(id=2, name="Genre 2")

    genres = {
        1: genre_1,
        2: genre_2
    }

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=genres.values())
    genre_dao.create = MagicMock(return_value=Genre(id=1, name='Genre 1'))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao

@pytest.fixture()
def movie_dao():

    movie_dao = MovieDAO(db.session)

    movie_1 = Movie(id=1, title="Movie 1", description="text 1", trailer="trailer 1", year=2000 , rating=3.5, genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title="Movie 2", description="text 2", trailer="trailer 2", year=2002 , rating=4.5, genre_id=2, director_id=2)

    movies = {
        1: movie_1,
        2: movie_2
    }

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=movies.values())
    movie_dao.create = MagicMock(return_value=Movie(id=1, title="Movie 1"))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao
