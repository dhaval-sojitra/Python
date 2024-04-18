# #Fuctions
# # Add two elements using function
# def sum(a,b):
#     add = a + b 
#     print("Sum of give numbers is :",add)
# sum(10,10)

# # Returning result from a function
# def sum(a,b):
#     add = a+b
#     return add
# q = sum(20,10)
# print("Sum of give numbers is :",q)

# #find the value is odd or even
# def find(v):
#     if(v%2 == 0):
#         print("Given value is Even.")
#     else:
#         print("Given value is Odd.")
# a = int(input("Enter Any Value :"))
# find(a)

# #Program to pass integer to a function and modify it
# def change(i):
#     i = 5
#     print("Value of Inside the function is :",i)

# i = 10;
# change(i)
# print("Value of Outside the function is :",i)

# #For Mutable Object
# def change(lst):
#     lst.append(10)
#     print(lst)
# lst = [1,2,3,4]
# change(lst)
# print(lst)

# #Two Sum
# lst = [10,20,30,40,50]
# print("List :",lst)
# a=int(input("Enter number of Sum :"))
# for i in range(len(lst)):
#     sum = lst[i]+lst[i+1]
#     try:
#         if sum==a:
#             # print('lst[',i,'] + lst[',i+1,']')
#             print("list[{}] + list[{}] = {}".format(i,i+1,a))
#             break    
#     except IndexError:
#         print("Elements not found..")
        
# #Find Sum of two lists
# l1 = []
# l2 = []
# num1 = ""
# num2 = ""
# val1 = int(input("How many elements you want to enter in first List :"))
# for i in range(val1):
#     a = int(input("Enter {} Element :".format(i)))
#     l1.append(a)

# print(l1)
# val2 = int(input("How many elements you want to enter in Second List :"))
# for i in range(val2):
#     a = int(input("Enter {} Element :".format(i)))
#     l2.append(a)
# print(l2)
# for i in range(len(l1)):
#     a = l1[i]
#     a =  str(a)
#     num1 = num1 + a
# for i in range(len(l2)):
#     b = l2[i]
#     b = str(b)
#     num2 = num2 + b    

# sum = int(num1) + int (num2)    
# print(num1, "+" ,num2)
# print("Sum = ",sum)


# #Pie chart 
# import matplotlib.pyplot as plt

# branch  = ['BCA','MCA','BBA','MBA','BA']
# student = [0,2500,150,2500,150]
# col = ['blue','green','yellow','red','pink']
# # plt.pie(student,labels=branch,colors=col)
# plt.plot(branch,student,color='black')
# plt.title("Atmiya University")
# plt.legend()
# plt.show()

# #file handling
# #opne a file
# f = open('file1','w')
# str1 = input("Enter Data..")
# f.write(str1)
# f.close()

# #read a extisting file
# f = open('file1','r')
# str1 = f.read()
# print(str1)
# f.close()

# #Append

# f = open('file1','a')
# str1 = input("Enter Data : ")
# while str1!='$':
#     if str!='$':
#         f.write(str1)
#         break
# f.close()

# dic = {"name" : "dhaval","city" : "Surat"}
# print(dic)
# print(dic.keys())
# print(dic.values())
# dic["name"] = "keval"
# print(dic)
# dic["age"] = 21
# print(dic)

# months = ["jan","feb","march","april","may"]
# print(months)
# cin = "jan" in months
# print(cin)
# nin = "dec" not in months
# print(nin)

# val = input("enter value :")
# val.split(" ")
# print(val)
# # print(val[0])
# print(val[2])

# import sys
# num1 = int(sys.argv[1])
# num2 = int(sys.argv[2])
# print(num1,"+",num2,"=",num1+num2)

# li = []
# no =int(input("How many ? "))
# for i in range(no):
#     val = input("enter :")
#     li.append(val)
# print(sorted(li))

# from numpy import *
# a=array([5,6,7,8] )
# print(a)

from array import *
a = array('i',[10,20,30,20,40])
# print(a)
# a.append(500)
# print(a)
# a.pop()
# print(a)
# a.remove(a[1])
# print(a)
# a.insert(2,200)
# print(a)
# print(a,a.reverse())
# li = list(a)
# print("list ",li)
val = int(input("enter element :"))
print(a.index(val))
















