import os,zipfile

f = zipfile.ZipFile('/home/lf/practice.zip','w')

for i in os.listdir():

    f.write(i,i)

f.close()

