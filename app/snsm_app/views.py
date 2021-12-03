from flask import render_template
from .models.forms.auth import LoginForm
from .models.database import get_sauveteurs

from flask import Blueprint, render_template, redirect, request, current_app

import hashlib

index = Blueprint('index', __name__, url_prefix="/")


@index.route("/")
def hello():
    return render_template(
        "home.html",
        title="bonjour à tous les amis 2")


@index.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        content = hashlib.sha256(form.password.encode()).digest()
        print(content)
        return redirect('/')
    return render_template('login.html', form=form, title="Se connecter")


@index.route("/logout")
def logout():
    return "TODO LOGOUT"


@index.route("/bateaux")
def bateaux():
    return render_template(
        "bateau.html",
        title="bonjour à tous les amis 2",
        personnage_pas_important={
            "Patron": "NomPatron", "Sous-Patron": "Nom du Sous-patron", "armement": ["Nom1", "Nom2", "Nom3"]},
        DATE="01/01/01",
        STATS_VIE={"mort": 2, "vivant": 3},
        NOM_BATEAU="LES TROIS SOEURS"
    )


@index.route("/sauvetages")
def sauvetages():
    return "TODO"


@index.route("/sauveteurs")
def sauveteurs():
    return render_template(
        "sauveteurs.html",
        title="Les sauveteurs",
        sauveteurs = get_sauveteurs(current_app.config["DB"])
    )


@index.route("/bateau/<int:id>")
def bateau(id):
    return "l"


@index.route("/personne/<int:id>")
def personne(id):
    return "<h1>%d</h1>" % id


@index.route("/sauvetage/<int:id>")
def sauvetage(id):
    return "<h1>%d</h1>" % id
