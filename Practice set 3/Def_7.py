s1 = int(input("Enter Marks Of Student 1 :"))
s2 = int(input("Enter Marks Of Student 2 :"))
s3 = int(input("Enter Marks Of Student 3 :"))
s4 = int(input("Enter Marks Of Student 4 :"))

if s1>s2 and s1>s3 and s1>s4:
    print("Student 1's Marks is Highest.")
elif s2>s1 and s2>s3 and s2>s4:
    print("Student 2's Marks is Highest.")
elif s3>s1 and s3>s2 and s3>s4:
    print("Student 3's Marks is Highest.")
else:
    print("Student 4's Marks is Highest.")
