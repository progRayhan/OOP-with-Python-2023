class Student:
    roll = ""
    gpa = ""

    def display(self):
        print(f"Roll : {self.roll} GPA : {self.gpa}")

rana = Student()

rana.roll = 105
rana.gpa = 4.21
rana.display()

rana.roll = 203
rana.gpa = 4.57
rana.display()
# this continuously value assign is boring
# so I can build a new Method for this