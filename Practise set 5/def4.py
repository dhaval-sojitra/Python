# 4. Accept the string from the user; allow user to choose from the following options and perform
# the task as per user’s choice. i). Convert to the upper case, ii). Convert to the lower case, iii).
# Convert to the swap case, iv). Convert to the title case

a = input("Enter any string :")
print("---------------------Choices---------------------")
print("1.Convert to UPPER CASE\n2.Convert to the lower case\n3.Convert to the swap case\n4.Convert to the title case")
print("---------------------------------------------------")
choice = int(input("Enter Your Chice :"))
print("---------------------------------------------------")
if choice==1:
    print(a,"In UPPER CASE :")
    print(a.upper())
elif choice==2:
    print(a,"In lower case :")
    print(a.lower())
elif choice==3:
    print(a,"In Swap Case :")
    print(a.swapcase())
elif choice==4:
    print(a,"In  Title Case :")
    print(a.title())
else:
    print("Enter Valid Choice..")
