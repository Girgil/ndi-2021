from wtforms import Form, StringField, PasswordField, validators


class LoginForm(Form):
    username = StringField("Nom d'utilisateur",  [
        validators.DataRequired(),
    ])
    password = PasswordField('Mot de passe', [
        validators.DataRequired(),
    ])
