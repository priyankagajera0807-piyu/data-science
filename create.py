import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db1"
)

mycursor = mydb.cursor()
mycursor.execute("insert into student (stud_id,name) values(102,'Vihan'),(103,'Meet')")
mydb.commit()
print("Record Inserted.....!")

mycursor.close()
mydb.close()
