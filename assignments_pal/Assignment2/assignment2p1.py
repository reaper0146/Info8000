#Soumya Pal
#Assignment 2 part 1

import math

def solvePythagorean(a,b='none'):
  if b == 'none':
    b = a
  diag = math.sqrt((a**2)+(b**2))
  return diag

print(solvePythagorean(3,4))
print(solvePythagorean(1,2))
print(solvePythagorean(5))
print(solvePythagorean(-3))