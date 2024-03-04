# 14) Accept numbers from the user; display the sum of the entered numbers.
print("Enter Numbers and get sum of given numbers,for stop insering numbers please enter 0.")
a=1
num = None
sum = 0
while num!=0:
    num = int(input("Enter Number: "))
    sum += num
    a+=1
print("Sum of your entered numbers is :",sum)
   
