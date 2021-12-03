from flask import render_template
from flask.helpers import url_for
from .models.forms.auth import LoginForm, RegisterForm
from .models.database import get_sauveteurs, insert_user, get_bateaux

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
        return redirect('/')
    return render_template('login.html', form=form, title="Se connecter")


@index.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        content = hashlib.sha256(form.password.data.encode()).hexdigest()
        s = current_app.config['SESSION']
        insert_user(s, form.username.data, form.email.data, content)
        s.remove()
        return redirect(url_for("index.login"))
    return render_template('register.html', form=form, title="S'inscrire")


@index.route("/logout")
def logout():
    return "TODO LOGOUT"


@index.route("/bateaux")
def bateaux():
    s = current_app.config['SESSION']
    batals = get_bateaux(s)
    s.remove()
    return render_template(
        "corps_pages.html",
        title="Bateaux",
        bateaux=batals
    )


@index.route("/bateau/<int:id>")
def bateau(id):
    return render_template(
        "bateau.html",
        title="Bateaux - X",
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
    s = current_app.config['SESSION']
    sauveteurs = get_sauveteurs(s)
    s.remove()
    return render_template(
        "sauveteurs.html",
        title="Les sauveteurs",
        sauveteurs=sauveteurs
    )

@index.route("/personne/<int:id>")
def personne(id):
    return "<h1>%d</h1>" % id


@index.route("/sauvetage/<int:id>")
def sauvetage(id):
    return "<h1>%d</h1>" % id
