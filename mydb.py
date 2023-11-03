import mysql.connector

dataBase = mysql.connector.connect(
    user = 'root',
    passwd = '1994',
    host = 'localhost',
   
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE database1")

print("All Done")