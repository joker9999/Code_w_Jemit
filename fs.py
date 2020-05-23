import os
import shutil
import time
st= time.clock()        #starttime
#cwd= os.getcwd()
#print(cwd)
path="C:\\Users\\harsh\\Desktop\\Test"      #path in which files to be sorted are present
fpath="C:\\Users\\harsh\\Desktop\\Test"    #path in which files are to be sorted

if os.path.exists(fpath) is False:      #incase if the final destinaton folder doesnt exist
    os.mkdir(fpath)

dpath= os.listdir(path)     #list containing names of all files in the sourcepath in the form of strings
#file=[]
#print(len(dpath))
for i in dpath:
    if os.path.isdir(path+"\\"+i):      #to avoid folders
        dpath.remove(i)             #remove all folders from the path

file=[os.path.splitext(i)    for i in dpath] #if os.path.splitext(i)[1]!=""]       #list containing a list of tuples with the name and extensions as elements

ext=[]
for i in file[:]:
    ext.append(i[1])        #creating a list with extensions (there can be similar elements)

unique_ext= list(set(ext))      #converting ext into a list which contains unique elements only
k=len(unique_ext)

for i in range(len(file)+len(unique_ext)):      #looping through to create extension folders and also move the files respectively in the same loop
    if k!=0:
        k-=1
        n_path= os.path.join(fpath,((unique_ext[i][1:].capitalize())+" Files"))      #create a folder with the name of extension
        if os.path.exists(n_path) is False:     #incase if folder doesnt exist, create it
            os.mkdir(n_path)
    else:
        source= os.path.join(path,dpath[i-len(unique_ext)])     #selecting the file in the source folder
        dest= os.path.join(fpath,((file[i-len(unique_ext)][1])[1:].capitalize()+" Files"))      #selecting the folder in which the file is to be moved
        shutil.move(source,dest)    #moving the files

et=time.clock()     #end time
print(et-st)
