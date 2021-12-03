"""
    Permet de créer l'application.
"""


import os
import sqlite3
import traceback
from flask import Flask
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
    app.config['DB'] = sqlite3.connect(os.environ.get(
        'DATABASE_URL'))
    return app
