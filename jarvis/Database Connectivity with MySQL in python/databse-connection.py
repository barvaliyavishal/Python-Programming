import mysql.connector
mydb = mysql.connector.connect(host = 'localhost',user='root',passwd='root',database = 'vishal')

mycursor = mydb.cursor()

mycursor.execute("select * from student")

for i in mycursor:
    print(i)