import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),
            p
        )
    )

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URL')

db = SQLAlchemy(app)

@app.route("/")
def hello():
    return render_template(
        "home.html")


if __name__ == "__main__":
    app.run()
