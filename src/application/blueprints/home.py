import logging

import flask

from ..model import db, Post, User

bp = flask.Blueprint("home", __name__)


@bp.route("/")
def index():
    """Home page, displays the feed.

    Returns:
        [str]: Flask template, as HTML string
    """
    user = db.session\
        .query(User)\
        .first()

    posts = db.session\
        .query(Post)\
        .order_by(Post.created_at.desc())\
        .all()

    return flask.render_template(
        "home.html",
        user=user,
        posts=posts
    )
