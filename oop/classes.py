class Person:
    def __init__(self, first_name, last_name, age):
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.course = []
    def enrol_new_course(self, course):
        self.course.append(course)
        return f"Here is your list of courses: {self.course}"
    def __str__(self) -> str:
        return f"Your name is {self.firstname} {self.lastname} and your age is {self.age} and you have enrolled into {self.course}"
class Student(Person):
    def __init__(self, first_name, last_name, age,student_id):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
    def __str__(self) -> str:
        # return super().__str__()
        return f"Your name is {self.firstname} {self.lastname} and your age is {self.age} and you have enrolled into {self.course}"
class Undergraduate(Student):
    def __init__(self, first_name, last_name, age, student_id, major):
        super().__init__(first_name, last_name, age, student_id)
        self.major = major
class Graduate(Student):
    def __init__(self, first_name, last_name, age, student_id, major):
        super().__init__(first_name, last_name, age, student_id)
        self.major = major
    def enrol_new_course(self, course):
        if len(self.course) <5:
            return super().enrol_new_course(course)
        else:
            return f"Cannot enroll you to {course}. You have exceed {len(self.course)}"
person1 = Student('Alex', 'Guandaru', 27, 4376)
person2 = Graduate("Jane", "Maina", 55, 2381, "Economics")
person3 = Undergraduate("Ann", "Mucheru", 26, 3424, "Nursing")
person4 = Undergraduate("Anabel", "Wainaina", 26, 3424, "Doctor")
person5 = Graduate("James", "Smart", 26, 3424, "Electrician")
persons = [person1,person2,person3,person4,person5]

# person1.enrol_new_course("BE")
# print(person1)

# print(person2.enrol_new_course("Mathematics"))
# print(person2.enrol_new_course("English"))
# print(person2.enrol_new_course("Kiswahili"))
# print(person2.enrol_new_course("Biology"))
# print(person2.enrol_new_course("Economics"))
# print(person2.enrol_new_course("Morphology"))
# print(person2.enrol_new_course("astronomy"))


# print(person1.enrol_new_course("Mathematics"))
# print(person1.enrol_new_course("English"))
# print(person1.enrol_new_course("Kiswahili"))
# print(person1.enrol_new_course("Biology"))
# print(person1.enrol_new_course("Economics"))
# print(person1.enrol_new_course("Morphology"))
# print(person1.enrol_new_course("astronomy"))

for person in persons:
    print(person)
    print(person.enrol_new_course('Mathematics'))
    print(person)
    print()
