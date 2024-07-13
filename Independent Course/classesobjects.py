class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    def calculate_average(self):
        average = sum(self.marks)/len(self.marks)
        return average


james = Student('James', 'Alliance')
simon = Student('Simon', 'OBJEC')
james.marks.append(80)
james.marks.append(70)
james.marks.append(60)
print(james.calculate_average())

#class method and static method

