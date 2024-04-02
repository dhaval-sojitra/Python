# # binary to decimal
# num1 = "0b1001"
# dnum1 = int(num1,2)
# print("Binary to decimal : ",dnum1)

# #Octal to decimal
# num2  ="0o214"
# onum2 = int(num2,8)
# print("Octal to Decimal : ",onum2)

# #Hexadecimal to decimal
# num3 = "2e"
# hnum3 = int(num3,16)
# print("Hexadecimal to Decimal : ",hnum3)

# #to add two numbers using function
# def sum(a,b):
#     sum = a+b;
#     print("The sum of two digits is :",a+b)
# sum(10,20)

# #Returing result from a function 
# def sum(a,b):
#     add = a+b;
#     return(add)
# a = sum(10,20)
# print("The sum of two digits is :",a)

# #find the value is odd or even
# def check(num):
#     if num%2==0:
#         print("the number is even")
#     else:
#         print("the number is odd")

# val = int(input("Enter Any Number : "))
# check(val)

# #rerturing multiple values from a function
# def cal(a,b):
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div

# a = int(input("Enter First Value :"))
# b = int(input("Enter Second Value :"))
# add,sub,mul,div = cal(a,b)
# print("Addition of two numbers is :",add)
# print("Substraction of two numbers is :",sub)
# print("Multiplication of two numbers is :",mul)
# print("Divison of two numbers is :",div)

#program to pass integer to a function and modify it
def mod(a):
    a=7
    print("The value of a inside the function is :",a)
a=10
print("The value of a outside the function is :",a)
mod(a)