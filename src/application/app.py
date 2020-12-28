import os
import babel

from flask import Flask

from . import cli
from . import jinja_filters
from .model import db, session


def create_app():
    """ Flask app factory that creates and configure the app.
    Args:
        test_config (str): python configuration filepath
    Returns: Flask application
    """
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    db.init_app(app)

    # blueprints
    from .blueprints import home, user
    app.register_blueprint(home.bp)
    app.register_blueprint(user.bp, url_prefix="/users")

    # register cli commands
    app.cli.add_command(cli.init_db_command)

    # register filters
    app.jinja_env.filters["datetime"] = jinja_filters.format_datetime

    # request handlers
    @app.after_request
    def commit_db_session(response):
        session.commit()
        return response

    return app
