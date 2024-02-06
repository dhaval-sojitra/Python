li = int(input("Enter Liters of Water : "))

if li<90:
    print("Your Water bill is : 0 Rs.")
elif li>90 and li<=150:
    print("Your Water bill is : ",li*2)
elif li>150 and li<=250:
    print("Your Water bill is : ",li*5)
elif li>250:
    print("Your Water bill is : ",li*10)
else: 
    print("Enter Valid Liters of Water")