#List Datatype
a=[2,5,8,'a','Dhaval',-255]
print(a)
print(a[3])
print(a[3:5])

#Tuple Datatype
a=(5,8,'z','Dhaval',-255)
print(a)
print(a[2])

#Sets Datatype
a={2,4,5,8,10,'a','Dhaval',-255}
print(a)
#update set values
a.update([12,11])
print(a)
#Removing elements
a.remove(-255)
print(a)
#Converting list to set
list=[4,566,6,7]
print(list)
st=set(list)
print(st)

#Frozenset Datatype
a={2,4,65,7,6,5,98,56,4,6}
print(a)
fs=frozenset(a)
print(fs)

#Mapping Datatype(Dictionary)
a={'id' : '3136','Name' : 'Dhaval','City' : 'Rasnal'}
print(a)
#Empty Dictionary
b={}
print(b)
b[1]='Dhaval'
print(b)
#Retriving Only key
print(a.keys())
#Retriving Only value
print(a.values())
#Updateing vlaue using key
a['City'] = 'Surat'
print(a)
#Deleting element
del a['City']
print(a)























