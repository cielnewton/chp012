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


sql = "DELETE FROM student WHERE age = 47 and prenom = 'Gregory'"


cursorObject .execute(sql)
dataBase.commit()
dataBase.close()
