from .app import db

class Personne(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prenom = db.Column(db.String(50))
    nom = db.Column(db.String(50))
    dateNaissance = db.Column(db.Date()) 
    dateDeces = db.Column(db.Date())
    etatCivil = db.Column(db.Text())
    descendancePersonne = db.Column(db.Text())

    def __repr__(self):
        return "<Personne (%d) %s %s>" % (self.id, self.prenom, self.nom)

class Sauveteur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idPersonne = db.Column(db.Integer, db.ForeignKey("personne.id"))
    personne = db.relationship("Personne", uselist=False)

    def __repr__(self):
        return "<Sauveteur (%d) %s %s>" % (self.id, self.personne.nom, self.personne.prenom)

class Equipage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idSauveteur = db.Column(db.Integer, db.ForeignKey("sauveteur.id"))

class Appartenir(db.Model):
    idPersonne = db.Column(db.Integer, db.ForeignKney(""), primary_key=True)

    





