# Python program to connect
# to mysql database


import mysql.connector


# Connecting from the server
conn = mysql.connector.connect(user = 'root',
                            password = "",
							host = 'localhost',
							database = 'snir_db',
                            port = 3306,
                            )

print("Connecté")

# Disconnecting from the server
conn.close()
