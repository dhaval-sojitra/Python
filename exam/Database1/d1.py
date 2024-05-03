import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password = "",database = "mypy")
cursor = con.cursor()

create = "create table stud2(id int,name varchar(255),city varchar(255))"
cursor.execute("create")
print("table created")

query = "insert into stud values(%s,%s,%s)"
data = [(1,'dhaval','surat'),(2,'keval','surat')]
cursor.executemany(query,data)

update = "update stud set city = 'rajkot' where name = 'dhaval'"
cursor.execute(update)
con.commit()

delete = "delete from stud where id = 2"
cursor.execute(delete)
con.commit()

select = "select * from stud"
cursor.execute(select)
rs = cursor.fetchall()
for i in rs:
    print(i)