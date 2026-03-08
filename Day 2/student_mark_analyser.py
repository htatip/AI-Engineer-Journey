name = input("Enter your name: ")
marks = []

for i in range(3):
    mark = int(input("Enter marks: "))
    marks.append(mark)

total = sum(marks)
average = total/len(marks)
highest = max(marks)
lowest = min(marks)

print("Student:", name)
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)