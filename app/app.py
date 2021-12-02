from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template(
        "home.html",
        title = "bonjour à tous les amis 2")


if __name__ == "__main__":
    app.run()
