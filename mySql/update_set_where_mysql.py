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


sql = "UPDATE student set age = 47 WHERE nom = 'KORRI'"


cursorObject .execute(sql)
dataBase.commit()
dataBase.close()
