#Soumya Pal
#Assignment 2 part 6

import numpy as np

def sumUntil(a, maxSum):
  temp = []
  while len(temp) < len(a):
      for i in a:
        if np.sum(temp) + i <= maxSum: # and len(temp) < len(a):
          #print(i)
          temp.append(i)
        #print(temp)
        else:
          #print(np.sum(temp))
          return np.sum(temp), len(temp)
  if len(temp) == len(a):
    return np.sum(temp), len(temp)

print(sumUntil([1,2,3,4,5,6],7))
print(sumUntil([8,-4,10,1,9],14))
print(sumUntil([],7))
print(sumUntil([9,3,18,1,26],30))
print(sumUntil([1,7,4,15,28],100))