def create_app():
    from flask import Flask, render_template
    app = Flask(__name__)

    from .snsm_app.views import index
    app.register_blueprint(index)
    return app
