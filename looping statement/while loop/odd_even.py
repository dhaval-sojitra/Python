b=int(input("Enter 1 for Odd number || 2 for Even number :"))
if b==1:
    a=1
    while a<=10:
        if(a%2!=0):
            print(a)
        a+=1
elif b==2:
    a=1
    while a<=10:
        if(a%2==0):
            print(a)
        a+=1
else:
    print("Please enter valid number")
