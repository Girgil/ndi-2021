"""
    Permet de créer l'application.
"""


import os
from flask import Flask
from .snsm_app.views import index
from .snsm_app.commands import bp
from .snsm_app.models.database import db


def create_app():
    """
        Créer l'application
    """
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        'SQLALCHEMY_DATABASE_URL')

    app.register_blueprint(index)
    app.register_blueprint(bp)
    db.init_app(app)

    return app
