#deleteFilesMoreThen30Days --> Will delte files in a spefied folder which is more than 80 MB and greater than 30 deleteFilesMoreThen30Days

import os, shutil, time, sys

currentPath = os.getcwd()
print ('Hi, We are in folder \n' + currentPath + ' \nEnter the path to delete files more then 30 days and greater than 80 MB')
dirToBeCleaned = input()
os.chdir(dirToBeCleaned)
print ('Current Path\n' + os.getcwd())

now = time.time()
print (now)
for files in os.listdir('.'):
    #print (os.stat(files))
    if os.stat(files).st_mtime < now -  3 * 86400:
        os.remove(files)