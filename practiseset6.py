# #1. Create a file with file name sample.txt, accept some data from the user and store it in the file.
# f= open("sample.txt","w")
# str1 = input("Enter Content which you enter in file :")
# if f.write(str1):
#     print("Data Write Successfully..")
# else :
#     print("Data Write Failure..")
# f.close()

# #2. Display the data stored in the sample.txt file (created in question 1).
# f = open("sample.txt","r")
# str1 = f.read()
# print("File content : ",str1)
# f.close()

# #3. Accept some data from the user and append it into the file sample.txt (created in question 1),
# #also the data in the file.
# f = open("sample.txt","a")
# str1 = input("Enter Content which you append in file : ")
# if f.write(str1):
#     print("File appended Successfully..")
# else :
#     print("File appended Failure..")

# # 4. Accept the file name from the user, check the availability of the file: i). If the file exists display
# # the data on the screen, ii). If the file is not available, display the appropriate message.

# import os
# fname = input("Enter File Name : ")
# if os.path.isfile(fname):
#     f = open(fname,'r')
#     str1 = f.read()
#     print("File content :",str1)
# else : 
#     print("File Not Found..")

# 5. Accept the file name from the user, check the availability of the file:
# a. If the file exists, display: i). No. of characters, ii). No. of words and iii). No. of lines
# b. If the file does exist, than display the appropriate message.

import os
fname = input("Enter File Name : ")
if os.path.isfile(fname):
    f= open(fname,'r')
    str1 = f.read()
else : 
    print("File Not Found..")    
char = 0
line = 0
words = 0
for i in str1:
    char+=1
    if i==" " or i=="\n":
        words += 1
    if i=="\n":
        line += 1
print("No Of Charactera in the File :",char)
print("No of words in the file :",words+1)
print("No of lines in the file :",line+1)

# 6. Create and open the binary file with ‘with’ option. Store names of all the subjects you study in
# semester 2. Ask user to enter the subject number they wanted to see and display that subject
# name.

