import sqlite3
import os

def afficher():
    conn = sqlite3.connect("madatabase.db")
    c = conn.cursor()

    c.execute("UPDATE personne SET prenom = ? WHERE nom = 'Laurent'",("Steeve",))

    conn.commit()
    conn.close()

afficher()
# os.system("pause")