# 10. Accept numeric elements from the user, store it to the array and display. Ask user to enter
# search element. Display the position of the searched element.

from array import *
no = int(input("How many elements you want to enter? "))
arr = array('i',[])
for i in range(no):
    item = int(input("Enter {} element :".format(i+1)))
    arr.append(item)
print("Array :\n",arr)
print("--------------------------------------------")
search = int(input("Search Element : "))
print("Position of  the searched element is: ",arr.index(search))