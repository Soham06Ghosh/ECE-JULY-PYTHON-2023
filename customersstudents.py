import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="soham"
)

mycursor= mydb.cursor()

sql = "INSERT INTO customers(name,address) VALUES (%s,%s)"
val = ("sohom","kolkata")
mycursor.execute(sql,val)

sql_2 = "INSERT INTO customers(name,,gmail,address,gender) VALUES (%s,%s,%s,%s)"
val_2 =("test1","addressTest","test@gmail.com","Male")
mycursor.execute(sql_2, val_2)

mydb.commit()
print(mycursor.rowcount,"record inserted.")