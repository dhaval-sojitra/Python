# 16) Accept numbers from the user; find and display number of zeros available in the number.

num = int(input("Enter Any number : "))
count = 0
n_str = str(num)
for i in n_str:
    if i=='0':
        count +=1 
        
print("Numbers of 0 in given number is :",count)
