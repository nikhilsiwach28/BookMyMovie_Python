from flask import Blueprint

movie = Blueprint("movie", __name__)

from . import movie_routes