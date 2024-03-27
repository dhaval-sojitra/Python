# 1. Create a list containing several strings. Take input from the user (search string); display whether
# entered string is available in the list or not.

list = ["dhaval", "keval", "jimit", "jaydeep", "divyaraj"]
serach = input("Enter a string :")

if serach in list :
    print(serach , "Available in list.")
else : 
    print(serach , "Not Available in list.")