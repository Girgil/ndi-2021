from typing import List
from sqlite3 import Connection


class Personne(object):
    def __init__(self, id, nom, prenom, date_naissance, date_mort, etat_civil, descendance):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.date_mort = date_mort
        self.etat_civil = etat_civil
        self.descendance = descendance


class Sauveteur(object):
    def __init__(self, id, personne):
        self.id = id
        self.personne = personne


class Bateau:
    def __init__(self, id, typeB, nom):
        self.id = id
        self.type = typeB
        self.nom = nom

    def __repr__(self):
        return str(self.id) + " " + self.type + " " + self.nom


def get_sauveteurs(conn: Connection) -> List[Sauveteur]:
    c = conn.execute("SELECT * FROM SAUVETEUR NATURAL JOIN PERSONNE")
    personnes = list()
    for row in c:
        personnes.append(Sauveteur(
            row[0],
            Personne(
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7]
            )))
    c.close()
    return personnes


def get_bateaux(conn):
    bateaux = list()
    data = conn.execute("select * from bateau")
    for raw in data:
        bateaux.append(Bateau(raw[0], raw[1], raw[2]))
    return bateaux
