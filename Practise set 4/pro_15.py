# 15) Accept numbers from the user; display the count of the entered numbers.

print("Please Enter Numbers,For stop entring numbers enter 0.")
count = 0
a=None
while a!=0:
    b = int(input("Enter Number : "))
    if(b==0):
        break
    count += 1
print("You Entered ",count," Numbers.")
