from typing import Optional
from sqlite3 import Connection

class Bateau:

    def __init__(self, id, typeB, nom):
        self.id = id
        self.type = typeB
        self.nom = nom

    def __repr__(self):
        return str(self.id) + " " + self.type + " " + self.nom

def get_bateaux(conn):
    bateaux = list()
    data = conn.execute("select * from bateau")
    for raw in data:
        bateaux.append(Bateau(raw[0],raw[1],raw[2]))
    return bateaux



 
        
        
