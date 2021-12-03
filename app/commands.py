from .app import app, db
from .models import Personne

@app.cli.command()

def createDb():
    '''Creates the tables'''
    db.create_all()
    db.session.commit()