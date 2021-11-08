import sqlite3

def ajouter_bdd():    
        conn = sqlite3.connect("madatabase.db")
        c = conn.cursor()

        c.execute("DROP TABLE personne")

        conn.commit()
        conn.close()
        print("La table a été supprimée")
        
ajouter_bdd()