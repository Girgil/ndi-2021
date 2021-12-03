from flask import Flask, render_template
app = Flask(__name__)


@app.route("/bateau")
def bateau():
    return render_template(
        "bateau.html",
        title = "bonjour à tous les amis 2",
        personnage_pas_important = {"Patron":"NomPatron","Sous-Patron":"Nom du Sous-patron","armement":["Nom1", "Nom2", "Nom3"]},  
        DATE = "01/01/01",
        STATS_VIE = {"mort": 2, "vivant": 3},
        NOM_BATEAU = "LES TROIS SOEURS"
        )


if __name__ == "__main__":
    app.run()
