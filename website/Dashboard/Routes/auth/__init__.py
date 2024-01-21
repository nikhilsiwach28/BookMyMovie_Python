from flask import Blueprint 

auth = Blueprint("flask",__name__)

from . import auth_routes