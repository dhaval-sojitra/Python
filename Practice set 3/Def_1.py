salary = int(input("Enter Basic Salary :"))

print("------------------------------------------")

print("Your Basic Salary is %i"%salary)
print("------------------------------------------")
ta=(salary*4)/100
print("TA : ",ta)
da=(salary*30)/100
print("DA : ",da)
hra=(salary*15)/100
print("HRA : ",hra)
salary=salary+ta+da+hra
tax=(salary*3)/100
pf=(salary*12)/100
print("Tex :",tax)
print("PF :",pf)
print("------------------------------------------")

salary=salary-tax-pf
print("On hand Salary is : ",salary)