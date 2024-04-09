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


#Pie chart 
import matplotlib.pyplot as plt

branch  = ['BCA','MCA','BBA','MBA','BA']
student = [100,50,50,25,150]
col = ['blue','green','yellow','red','pink']
plt.pie(student,labels=branch,colors=col)
plt.title("Atmiya University")
plt.legend()
plt.show()

























