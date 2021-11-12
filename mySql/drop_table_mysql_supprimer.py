# importing required library
import mysql.connector

# connecting to the database
dataBase = mysql.connector.connect(
					host = "localhost",
					user = "root",
					passwd = "",
					database = "snir3_db" )

# preparing a cursor object
cursorObject = dataBase.cursor()

# creating table
studentRecord = "DROP TABLE student"

# table created
cursorObject.execute(studentRecord)

# disconnecting from server
dataBase.close()
