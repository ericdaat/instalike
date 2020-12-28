import logging

import flask

from ..model import db, User, Post

bp = flask.Blueprint("user", __name__)


@bp.route("/<string:username>")
def user(username):
    """Displays a user's profile.

    Args:
        username (str): username (e.g "bob")

    Returns:
        str: flask template as HTML string
    """
    user = db.session\
        .query(User)\
        .filter(User.username==username)\
        .first()

    return flask.render_template(
        "user.html",
        user=user
    )
