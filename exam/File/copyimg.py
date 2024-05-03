#Open the file in a Binary mode
f1=open('Python Syllabus_Pg1.png','rb')
f2=open('syllabus.png','wb')
#Read bytes from f1 and write it to f2
bytes=f1.read()
f2.write(bytes)
#Close the files
f1.close()
f2.close()