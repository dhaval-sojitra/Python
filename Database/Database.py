import sqlite3
con = sqlite3.connect('mydb.dp')
# con.execute('create table stude_data(roll integer,name varchar)')
# print('Table Created')

# con.execute("""insert into stude_data values 
#             (1,'Dhaval'),
#             (2,'Jimit'),
#             (3,'Keval')""")
# print("Record Inserted Successfully") 
# con.commit()

# cursor = con.execute('select * from stude_data')
# for i in cursor:
#     print(i)

# cursor = con.execute('select * from stude_data where roll >2')
# for i in cursor:
#     print(i)

# sq_up = "update stude_data set name='Yash' where  roll =3"
# con.execute(sq_up)
# cursor = con.execute('select * from stude_data')
# for i in cursor:
#     print(i)

sq_del = "delete from stude_data where roll =3"
cursor = con.execute(sq_del)
for i in cursor:
    print(i)
cursor = con.execute('select * from stude_data')
for i in cursor:
    print(i)
