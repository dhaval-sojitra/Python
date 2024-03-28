# 11. Take two arrays enter 5 digits in both arrays. Compare the corresponding element from each
# array and display only the bigger number.

from array import *
a = array('i', []);
b = array('i', []);
print("Enter 1st Array's Elements :")
for i in range(5):
    item = int(input("Enter Element {} :".format(i+1)))
    a.append(item)
print("Array 1 :\n",a)
print("-------------------------------------------")
print("Enter 2nd Array's Elements :")
for i in range(5):
    item = int(input("Enter Element {} :".format(i+1)))
    b.append(item)
print("Array 2 :\n",b)
print("-------------------------------------------")
print("Maximum Number Array")
print(max(a,b))

