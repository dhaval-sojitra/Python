# 17) Accept an integer from the user; tell user that whether entered number is even or odd.
ans = 'Y'
while ans.lower() == 'y':
    num = int(input("Enter any number :"))
    if num%2==0:
        print(num," is an Even Number.")
        print("--------------------------")
        ans = input("Do you want to check another number? Y/N ")
        if  ans.lower() != 'y' and ans.lower()!='n':
            while ans.lower() != 'y' and ans.lower()!='n':
                print("Please enter only Y or N..")
                ans = input("Do you want to check another number? Y/N ")

    else :
        print(num," is an Odd Number.")
        print("--------------------------")
        ans = input("Do you want to check another number? Y/N ")
        if(ans.lower() != 'y' and ans.lower()!='n'):
            print("Please enter only Y or N..")
            ans = input("Do you want to check another number? Y/N ")
