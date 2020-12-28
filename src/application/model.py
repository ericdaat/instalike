import uuid
from datetime import datetime
from flask.helpers import total_seconds

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import EmailType

db = SQLAlchemy()
session = db.session

Follows = db.Table(
    "follows",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("followed_user_id", db.Integer, db.ForeignKey("users.id"))
)

Likes = db.Table(
    "likes",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("post_id", db.Integer, db.ForeignKey("posts.id"))
)


class Comments(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))

    user = db.relationship("User", back_populates="comments")
    post = db.relationship("Post", back_populates="comments")


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(EmailType(), unique=True, nullable=False)
    avatar = db.Column(db.String(40))

    fullname = db.Column(db.String(20))
    bio = db.Column(db.Text())

    posts = db.relationship("Post", back_populates="user")

    likes = db.relationship(
        "Post",
        secondary=Likes,
        back_populates="likes"
    )

    comments = db.relationship("Comments", back_populates="user")

    follows = db.relation(
        "User",
        secondary=Follows,
        primaryjoin=Follows.c.user_id==id,
        secondaryjoin=Follows.c.followed_user_id==id,
        backref="children"
    )

    followers = db.relation(
        "User",
        secondary=Follows,
        primaryjoin=Follows.c.followed_user_id==id,
        secondaryjoin=Follows.c.user_id==id,
        backref="parents"
    )


    def __repr__(self):
        return "<User %r>" % self.username


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    content = db.Column(db.Text())
    picture = db.Column(db.String(50))

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="posts")

    likes = db.relationship(
        "User",
        secondary=Likes,
        back_populates="likes"
    )

    comments = db.relationship("Comments", back_populates="post")
