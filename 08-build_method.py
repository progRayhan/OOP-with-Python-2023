class Student:
    roll = ""
    gpa = ""

    # build method
    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll} GPA : {self.gpa}")

anik = Student()

anik.set_value(205, 4.2)
anik.display()

anik.set_value(405, 4.9)
anik.display()