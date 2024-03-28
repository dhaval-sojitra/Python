# 5. Allow users to enter multiple strings in the list; arrange the entered string into alphabetical
# order and display.
list = []
no = int(input("How many strings you want to enter in list ? "))
for i in range(no):
    item = input("Enter String {} : ".format(i+1))
    list.append(item)
print(sorted(list)) 