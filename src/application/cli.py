import click

from flask.cli import with_appcontext

from .setup import init_db


@click.command("init-db")
@with_appcontext
def init_db_command():
    """ Initialize the database by creating all tables,
    and insert dummy data.
    """
    init_db()
    click.echo("Initialized the database.")
