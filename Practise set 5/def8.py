# 8. Create a numeric array and perform following operations on it: Add 2 to each elements,
# Subtract 3 from each element, Multiply each element with 3, Divide each element by 2, Find
# max and min, find the average of all elements.

from numpy import *
arr = array([10,20,30,40])
print("Array :",arr)
print("-----------------------------------")
print("Add 2 to each elements :")
for i in range(len(arr)):
    arr[i] = arr[i] + 2
print(arr)
print("-----------------------------------")
print("Subtract 3 from each element :")
for i in range(len(arr)):
    arr[i] = arr[i]-3
print(arr)
print("-----------------------------------")
print("Multiply each element with 3 :")
for i in range(len(arr)):
    arr[i] = arr[i]*3
print(arr)
print("-----------------------------------")
print("Divide each element by 2")
for i in range(len(arr)):
    arr[i] = arr[i]/2
print(arr)
print("-----------------------------------")
print("Find max and min :")
print("Maximum value in array :",max(arr))
print("Minimum value in array :",min(arr))
print("-----------------------------------")
print("find the average of all elements")
print("Average of all eements :",average(arr))