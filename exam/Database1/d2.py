import sqlite3

con = sqlite3.connect('mydb.dp')

# create = "create table stud(id int,name varchar,city varchar)"
# con.execute(create)
# print("table created")

# insert = "insert into stud values(1,'dhaval','surat'),(3,'dhaval','surat'),(2,'dhaval','surat')"
# con.execute(insert)
# print("data inserted")
# con.commit()

fetch = "select * from stud"
data = con.execute(fetch)
for i in data:
    print(i)