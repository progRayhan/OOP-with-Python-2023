class Student:
    roll = ""
    gpa = ""

    # constructor
    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll} & GPA : {self.gpa}")


abdul = Student(203, 4.34)
abdul.display()

jalal = Student(302, 4.23)
jalal.display()