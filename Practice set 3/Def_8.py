amount = int(input("Enter Your Shopping Amount :"))

if amount<1500:
    print("Please purchase 1500 Amount to avail shipping charge of  Rs. 80/-")
    print("Please Pay :",amount," + 100 = ",amount+100)
elif amount>1500 and amount<3000:
    print("Please purchase 3000 Amount to avail shipping charge of  Rs. 50/-")
    print("Please Pay :",amount," + 70 = ",amount+100)
else:
    print("You Saved :",(amount*7/100))
    print("Please Pay :",(amount-(amount*7/100)))
