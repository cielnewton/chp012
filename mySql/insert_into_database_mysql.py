# importing required library
import mysql.connector
	
# connecting to the database
dataBase = mysql.connector.connect(
					host = "localhost",
					user = "root",
					passwd = "",
					database = "snir_db" )
	
# preparing a cursor object
cursorObject = dataBase.cursor()


sql = "INSERT INTO student (prenom,nom,age) VALUES (%s, %s, %s)"
val = [("Ilyas", "KORRI","46"),
       ("Charly", "SCHMITT","30"),
       ("Steeve", "DAUGER","42"),
       ("Louis", "LAURENT","26"), 
       ("Antony", "NANTOIS","29"), 
       ("Antoine", "LEFEVRE","27"), 

       ]

cursorObject .executemany(sql, val)
dataBase.commit()
dataBase.close()
