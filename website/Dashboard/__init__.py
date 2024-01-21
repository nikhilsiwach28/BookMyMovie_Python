# website/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    from website.Routes.user import user
    from website.Routes.movie import movie

    app.register_blueprint(user)
    app.register_blueprint(movie,url_prefix="/movie")

    # Add more blueprints as needed

    return app