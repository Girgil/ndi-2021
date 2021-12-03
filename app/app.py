from flask import Flask, render_template
app = Flask(__name__)


@app.route("/bateau")
def bateau():
    return render_template(
        "bateau.html",
        title = "bonjour à tous les amis 2",
        personnage_pas_important = ["Nom1", "Nom2", "Nom3"],
        DATE = "01/01/01"
        )


if __name__ == "__main__":
    app.run()
