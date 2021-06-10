#Soumya Pal
#Assignment 3 part 1
 
import os

dirlist = os.listdir("data")
for i in range(0,len(dirlist)):
    temp = "data/"+dirlist[i]
    #print("\n")
    print("\nFilename: " + dirlist[i])
    file = open(temp, "r", encoding="utf-8")
    data = file.read()
    #words = data.split()
    print('Num words:', len(data.split()))
    print('Num chars:', len(data))
