income = int(input("Enter Your Income :"))

if income<800000:
    print("You have Not  need to Pay any Tax")
elif income>=800000 and income<=1000000:
    print("You have need to Pay 15% Tax.")
    print("------------------------------------")
    print("Your Income :",income,"\n","Tax on Your Income :",(income*15)/100)
elif income>1000000 and income<=2000000:
    print("You have need to Pay 20% Tax.")
    print("------------------------------------")
    print("Your Income :",income,"\n","Tax on Your Income :",(income*20)/100)
else:
    print("You have need to Pay 30% Tax.")
    print("------------------------------------")
    print("Your Income :",income,"\n","Tax on Your Income :",(income*30)/100)