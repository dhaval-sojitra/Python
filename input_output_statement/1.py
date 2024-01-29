#Input and Output Statement 
print('Atmiya')
print('This is the \n new line')
print('the city is '+' Rajkot')
a='Rajkot'
print('the city is '+a)

#print (Variable list)Statemets
a,b=7,6
print(a,b)
print(a,b,sep='#')

print('Atmiya')
print('University')
print('Rajkot')

#Print output on the same line
print('Atmiya',end='')
print('University',end='')
print('Rajkot')

print('Atmiya',end='\t')
print('University',end='\t')
print('Rajkot')

#The print (object) statement
a=['a','Atmiya','Rajkot',25,True,10.24]
print(a)

#The print('String','Variable list) statement
a=7
print(a,'The value is printed here')
print('User has entered',a,'as an input')

#Print (formatted string)statement
#Print('Formatted string'%i(variable list))
a=7.2
print('Value =%i'%a)
#To print more than one integer value
a,b=7,25
print('a= %ib=%i'%(a,b))

#Inside the formatted string
n1,n2,n3=1,2,3
print('There number is {0},the number is {1},the number is {2}'.format(n1,n2,n3))

#Input Statements
a=input()
print(a)
name=input('Enter your name : ')
print(name)

#Restricting the input
sal=int(input('Enter your salary :'))
print(sal)

#Only second character will be stored in the variable and printed
char=input('Enter characters : ')[0]
print(char)

#Use of split() method
n1,n2,n3=[int(no) for no in input('Enter three integer values by giving space :
).split()]
print('The sum of 3 integer values is : ',n1+n2+n3)





