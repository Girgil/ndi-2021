"""
    Permet de créer l'application.
"""


import os
import sqlite3
from flask import Flask
from .snsm_app.views import index
from .snsm_app.commands import bp
from .snsm_app.models.database import Conn
from .snsm_app.models import database


def create_app():
    """
        Créer l'application
    """
    app = Flask(__name__)

    app.register_blueprint(index)
    app.register_blueprint(bp)
    database.db = sqlite3.connect(os.environ.get(
        'DATABASE_URL'))

    return app
