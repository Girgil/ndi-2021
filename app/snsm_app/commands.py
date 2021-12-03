from flask import Blueprint
from .models.database import db

bp = Blueprint('db', __name__)

@bp.cli.command()
def createDb():
    '''Creates the tables'''
    db.create_all()
    db.session.commit()