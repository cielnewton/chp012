# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root",
passwd ="",
database="snir3_db",
port=3306
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating database



request = """
        CREATE TABLE IF NOT EXISTS student
        (
            nom text,
            prenom text,
            age int     
        )
        """

cursorObject.execute(request)