from zipfile import *
#creating the zip file
f=ZipFile('sample.zip','w',ZIP_DEFLATED)
#Adding files to be zipped
f.write('arr.py')
f.write('ar2.py')
#close the zip file
f.close()
#Unzip
from zipfile import *
z=ZipFile('sample.zip','r')
z.extractall('D:\\Academics\\Python')