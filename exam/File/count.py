import os,sys
fname=input('Enter the file name to open: ')
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname+ 'does not exist')
    sys.exit()
cl=cw=cc=0
for line in f:
    words=line.split()
    cl=cl+1
    cw=cw+len(words)
    cc=cc+len(line)
print('Number of lines in a file is: ',cl)
print('Number of words in a file is: ',cw)
print('Number of charchters in a file is: ',cc)
f.close()