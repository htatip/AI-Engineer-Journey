import numpy as np

n= int(input("Enter number of students: "))

marks = []

for i in range(n):
    mark = int(input("Enter marks: "))
    marks.append(mark)

marks = np.array(marks)

avg = np.mean(marks)
highest = np.max(marks)
lowest = np.min(marks)
above_avg = np.sum(marks > avg)

print(avg,highest,lowest,above_avg)