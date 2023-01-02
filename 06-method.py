# method is look like function but write inside a class

class Student:
    roll = ""
    gpa = ""

    # method (have always self)
    def display(self):
        print(f"Roll : {self.roll} & GPA : {self.gpa}")

rana = Student()

rana.roll = 107
rana.gpa = 4.21

# call method
rana.display()