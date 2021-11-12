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

print("Displaying NAME and ROLL columns from the STUDENT table:")

# selecting query
query = "SELECT * FROM student"
cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
	print(x)

# disconnecting from server
dataBase.close()
