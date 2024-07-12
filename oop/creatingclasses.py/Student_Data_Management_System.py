class Student:
    def __init__(self,first_name, second_name, student_age):
        self.firstname = first_name
        self.secondname = second_name
        self.age = student_age
        self.courses = []
        self.enrolledsetudents = []
    def __str__(self) -> str:
        return f"Your name is {self.firstname} {self.secondname}."
    def add_course(self, course):
        self.courses.append(course)
        print(f'{course} added successfully')
        return self.courses
    def remove_course(self, course):
        if not course in self.courses:
            raise ValueError(f"Sorry. {course} is not present into your list of courses.")
        self.courses.remove(course)
        print(f"{course} has been successfully removed.")
        return self.courses
    def list_available_courses(self):
        for course in self.courses:
            print(course)
    def list_enrolled_students(self):
        for student in self.enrolledsetudents:
            print(self.firstname + ' ' + self.secondname)