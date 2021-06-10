#Soumya Pal
#Assignment 1 part 1

import numpy as np
import matplotlib.pyplot as plt

assignment_grades = [100,90,95,75,80,85,100,70,90,90,93,99,84,93,95]
assignment_average = round(np.mean(assignment_grades),1)
N = len(assignment_grades)
assignment_numbers = range(1,N+1)
assignment_labels = ["A"+str(x) for x in assignment_numbers]

plt.plot(assignment_numbers,assignment_grades)
plt.plot(assignment_numbers,assignment_grades, linestyle = "None", marker=".")
avg_line = plt.plot([1,N],[assignment_average,assignment_average])
plt.xticks(assignment_numbers,assignment_labels)
plt.title("assignment grades")
plt.xlabel("Assignment")
plt.ylabel("Grade")

plt.legend(avg_line,["Average ("+ str(assignment_average)+')'],loc='lower left')

plt.show()