from wtforms import Form, StringField, PasswordField, validators


class LoginForm(Form):
    username = StringField("Nom d'utilisateur",  [
        validators.DataRequired(),
    ])
    password = PasswordField('Mot de passe', [
        validators.DataRequired(),
    ])

class RegisterForm(Form):
    username = StringField("Nom d'utilisateur",  [
        validators.DataRequired(),
    ])
    password = PasswordField('Mot de passe', [
        validators.DataRequired(),
    ])
    email = PasswordField('Adresse email', [
        validators.DataRequired(),
    ])
