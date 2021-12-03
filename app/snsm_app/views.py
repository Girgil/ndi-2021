from flask import render_template
from .models.forms.auth import LoginForm

from flask import current_app, Blueprint, render_template, redirect, url_for, request

index = Blueprint('index', __name__, url_prefix="/")

@index.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        # TODO
        return redirect(url_for('/'))
    return render_template('login.html', form=form)



@index.route("/logout")
def logout():
    return "TODO LOGOUT"



@index.route("/")
def hello():
    return render_template(
        "personne.html",
        title="bonjour à tous les amis 2")