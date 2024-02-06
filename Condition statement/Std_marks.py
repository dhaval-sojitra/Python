s1 = int(input('Enter Student Mark 1 :'))
s2 = int(input('Enter Student Mark 2 :'))
s3 = int(input('Enter Student Mark 3 :'))
s4 = int(input('Enter Student Mark 4 :'))

if s1>s2 and s1>s3 and s1>s4:
    print("Student 1 Got the Highest Marks")
elif s2>s1 and s2>s3 and s2>s4:
    print("Student 2 Got the Highest Marks")
elif s3>s1 and s3>s2 and s3>s4:
    print("Student 3 Got the Highest Marks")
elif s4>s1 and s4>s2 and s4>s3:
    print("Student 4 Got the Highest Marks")
else:
    print("Enter Valid Marks")

