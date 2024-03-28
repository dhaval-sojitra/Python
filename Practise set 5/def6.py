# 6. Create a tuple and display it. Enter 25 at the third position and display it again.

tup = {10,20,30,40,50}
print("Tuple before add 25 at third position :\n",tup)
print("----------------------------------------------")
lst = list(tup)
lst[2] = 25
tup = tuple(lst)
print("Tuple after adding 25 at third position : \n",tup)