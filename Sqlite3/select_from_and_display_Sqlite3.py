import sqlite3
import os

def afficher():
    conn = sqlite3.connect("madatabase.db")
    c = conn.cursor()

    # c.execute("SELECT prenom FROM personne WHERE nom = 'Laurent'")
    c.execute("SELECT * FROM personne")
    # c.execute("SELECT * FROM personne")
    data_list = c.fetchall()
    print("Votre prénom est",data_list[-1][0])    

    # for element in data_list:
    #     print(element)

        # conn.commit()
    conn.close()

afficher()
os.system("pause")