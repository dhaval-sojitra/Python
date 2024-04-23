#check mysql connection
import mysql.connector
mydb = mysql.connector.connect(host ="localhost",user = "root",password = '',database = "marodatabase")
# print(mydb)

#create cursor
mcursor = mydb.cursor()
# mcursor.execute('create database marodatabase')
# print("Database created")

# mcursor.execute('show databases')
# for i in mcursor:
#     print(i)

# mcursor.execute('create table marutable(id int(3) primary key auto_increment, name varchar(255))')

# mcursor.execute("insert into marutable (id,name) values (2,'Dhaval Sojitra')")
query = "insert into marutable (id,name) values (%s,%s)"
val = [(5,'Jimit'),(6,'Keval')]
mcursor.executemany(query,val)

# mcursor.execute("select * from marutable")
# data = mcursor.fetchall()
# for i in data:
#     print(i)

# mcursor.execute("update marutable set name='keval' where id=4")
# mcursor.execute("delete from marutable where id = 2 ")
mydb.commit()
