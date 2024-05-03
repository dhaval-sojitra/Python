with open('sub.bin','wb') as f:
    n = int(input('Enter Number Of Subject in Sem - 2 :'))
    for i in range(n):
        sub = input('Enter Subject of Sem -2 : ')
        ln = len(sub)
        sub = sub.encode()
        f.write(sub)
with open('sub.bin','rb') as f:
    str = f.read()
    print("Sub : ",str.decode()," ")