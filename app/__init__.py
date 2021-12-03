"""
    Permet de créer l'application.
"""

from flask import Flask, render_template
from .snsm_app.views import index


def create_app():
    """
        Créer l'application
    """
    app = Flask(__name__)

    app.register_blueprint(index)
    return app
