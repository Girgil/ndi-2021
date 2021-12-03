from flask import render_template
from .models.forms.auth import LoginForm
from .models.database import db

from flask import Blueprint, render_template, redirect, request

index = Blueprint('index', __name__, url_prefix="/")


@index.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        # TODO
        return redirect('/')
    return render_template('login.html', form=form, title="Se connecter")


@index.route("/logout")
def logout():
    return "TODO LOGOUT"


@index.route("/")
def hello():
    return render_template(
        "personne.html",
        title="bonjour à tous les amis 2")


@index.route("/bateau/<int:id>")
def bateau(id):
    return "<h1>%d</h1>" % id


@index.route("/personne/<int:id>")
def personne(id):
    return "<h1>%d</h1>" % id


@index.route("/sauvetage/<int:id>")
def sauvetage(id):
    return "<h1>%d</h1>" % id
