import os
import shutil
import time
st= time.clock()
#cwd= os.getcwd()
#print(cwd)
path="C:\\Users\\harsh\\Desktop\\Test"
dpath= os.listdir(path)     #list containing names of all files in the path in the form of strings
#print(dpath)
file=[os.path.splitext(i)    for i in dpath]        #list containing a list of tuples with the name and extensions as elements
ext=[]

for i in file[:]:
    ext.append(i[1])        #creating a list with extensions

unique_ext= list(set(ext))      #converting ext into a list which contains unique extensions only

for i in unique_ext[:]:
    n_path= os.path.join(path,((i[1:].capitalize())+" Files"))      #create a folder with the name of extension
    if os.path.exists(n_path) is False:
        os.mkdir(n_path)

for i in range(len(file)):
    source= os.path.join(path,dpath[i])
    dest= os.path.join(path,((file[i][1])[1:].capitalize()+" Files"))
    #print("Source: ",source,"Destination: ",dest)
    #print(dest)
    #if os.path.exists(n_path) is False:
    #    os.mkdir(dest)
    #    shutil.move(source,dest)
    #else:
    shutil.move(source,dest)

et=time.clock()
print(et-st)
