from flask import Blueprint, current_app

bp = Blueprint('db', __name__)

@bp.cli.command()
def create():
    '''Creates the tables'''
    with open("app/sql/creation.sql") as f:
        file = f.read()
        current_app.config['DB'].executescript(file)