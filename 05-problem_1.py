class Student:
    roll = 1 # previous value
    gpa = 2 # previous value

puson = Student()
puson.roll = 5 # updated value (value overwriting)
puson.gpa = 10 # updated value (value overwriting)

print(f"Roll : {puson.roll} & GPA : {puson.gpa}")
print(f"Roll : {puson.roll} & GPA : {puson.gpa}")
print(f"Roll : {puson.roll} & GPA : {puson.gpa}")
# continuously - same code writing is boring, so I can use Methods in this situation