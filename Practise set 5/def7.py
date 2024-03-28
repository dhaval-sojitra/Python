# 7. Create a dictionary named library with following keys (Bookid, Title, Author, Price, Publisher).
# a. Display the dictionary, b. Display the name of Author, c. Display the Bookid
# d. Display the length of the dictionary, e. Update the price, f. Insert year as the new key
# and display the dictionary again.

dic = {"bookid" : 1,"title" : "Lipika","author" : "Rabindranath Tagore","price" : 200, "publisher": "Penguin Books"}
print("Display the dictionary\n",dic)
print("---------------------------------------------------------")
print("Display the name of Author\n",dic["author"])
print("---------------------------------------------------------")
print("Display the Bookid\n",dic["bookid"])
print("---------------------------------------------------------")
print("Display the length of the dictionary\n",len(dic))
print("---------------------------------------------------------")
print("Update the price\n")
print("Price before updating :",dic["price"])
dic["price"]=500
print("price after updating : ",dic["price"])
print("---------------------------------------------------------")
print("Insert year as the new key\n")
dic["year"] = "2020"
print(dic)
