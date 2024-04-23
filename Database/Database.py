import sqlite3
con = sqlite3.connect('mydb.dp')
# con.execute('create table stude_data(roll integer,name varchar)')
# print('Table Created')

con.execute("""insert into stude_data values 
            (1,'Dhaval'),
            (2,'Jimit'),
            (3,'Keval')""")
print("Record Inserted Successfully") 
con.commit()