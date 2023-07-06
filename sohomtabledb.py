import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="soham"
)

mysql_query = mydb.cursor()

mysql_query.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255),email VARCHAR(100),gender TEXT(50))")
print ("TABLE CREATED SUCCESSFULLY")
