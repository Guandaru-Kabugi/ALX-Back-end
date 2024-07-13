#inheritance
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    def calculate_average(self):
        average = sum(self.marks)/len(self.marks)
        return average
    #we want to return the same function even for the inherited class
    @classmethod
    #here, we had to add salary because the workingstudent class has salary.
    #we then created an origin for inheriting the school because we could not use the self.
    def friend(cls, origin, friend_name, salary):
        friend = cls(friend_name,origin.school, salary)
        return friend


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary
    
anna = Student('anna', 'nmit')
annmarie = WorkingStudent('annmarie', 'alx', 40000)
print(annmarie.name)
print(annmarie.salary)
#here, we focused on called the working student class and passing the method friend that now has anna as the origin
friend = WorkingStudent.friend(anna, 'Greg', 18000)
#these print statements help us see the individual details when friend is called.
print(friend.name)
print(friend.salary)
print(friend.school)