"""
    Permet de créer l'application.
"""


import os
import sqlite3
import traceback
from flask import Flask
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

try:
    from .snsm_app.views import index
    from .snsm_app.commands import bp
except:
    traceback.print_last()


def create_app():
    """
        Créer l'application
    """
    app = Flask(__name__)

    app.register_blueprint(index)
    app.register_blueprint(bp)

    app.config['DB'] = create_engine(os.environ.get(
        'DATABASE_URL'), poolclass=StaticPool)
    session_factory = sessionmaker(bind=app.config['DB'])
    app.config['SESSION'] = scoped_session(session_factory)
    return app