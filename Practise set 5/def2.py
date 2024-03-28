# 2. Accept the string from the user; display the message whether the entered string is palindrome
# or not.
a = input("Enter any string :")
reverse_string = a[::-1]

if a==reverse_string:
    print("Given string is palindrome.")
else:
    print("Given string is not palindrom.")