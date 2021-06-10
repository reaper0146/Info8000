#Soumya Pal
#Assignment 2 part 2

import numpy as np

s1 = '"hello world"'
s2 = "'hello world'"
s3 = '"\'hello world\'"'
s4 = 'hello\nworld'
s5 = '''This is a multiiline string:
hello
world
End of multiline string'''

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

course='INFO8000'
grades = [79,82,100,90]
student='Shomo Pal'

s6 = f"Course: {course}"
s7 = f"{student}'s grades: {grades}"
s8 = f"Highest grade: {np.max(grades)}"
s9 = f"Average: {np.mean(grades)}"

s10 = '''           ___          ___     
     ,-'``_.-'` \   / `'-._``'-.
   ,`   .'      |`-'|      `.   `.
 ,`    (    /\  |   |  /\    )    `.
/       `--'  `-'   `-'  `--'       \\
|                                   |
\\      .--.  ,--.   ,--.  ,--.      /
 `.   (    \/    \ /    \/    )   ,'
   `._ `--.___    V    ___.--' _,'
      `'----'`         `'----'`'''

print("\n")
print(s6)
print(s7)
print(s8)
print(s9)
print(s10)
