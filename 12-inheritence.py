class Section:

    # method 1
    def diba(self):
        a = 3
        b = 5
        print(a+b)

    # method 2
    def provati(self):
        c = 7
        d = 10
        print(c*d)


# inherit here
class School(Section):
    # now School class have all the methods of Section class
    pass

a = School()
a.diba()
a.provati()