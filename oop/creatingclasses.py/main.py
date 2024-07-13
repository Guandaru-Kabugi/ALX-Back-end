from Student_Data_Management_System import Student

def main ():
    print("Welcome to Student Data Management System.")
    firstname = input("What is your name? provide first name: ").title()
    secondname = input("What is your name? provide last name: ").title()
    check_user = True
    while check_user:
        try: 
            age = int(input("What is your age? ")) 
            student = Student(firstname,secondname,age)
            student_first_last_name = student.firstname + student.secondname
            student.enrolledsetudents.append(student_first_last_name)
            print(student)
            check_user = False
        except ValueError as e:
            print ("Enter a positive age integer", e)
    continue_asking = True
    while continue_asking:
        
        user_choice = input("Select 1 to add course, 2 to remove course, 3 to check list of available courses, 4 to check enrolled students, and 5 to exit, 6 to enrol a new student: ")
        match user_choice:
            case '1':
                try:
                    course_name = input("Enter course name to add: ").title()
                    student.add_course(course_name)
                except ValueError as e:
                    print("Input a string of characters", e)
            case '2':
                try:
                    student_name = input("What is your first and last name?: ")
                    if student_name in student.enrolledsetudents:
                        course_name_to_be_removed = input("Type name of the course you want removed: ").title()
                        student.remove_course(course_name_to_be_removed)
                    elif not student_name in student.enrolledsetudents:
                        raise ValueError("Your name is not in the enrolled list")
                except ValueError as e:
                    print(e)
            case '3':
                student.list_available_courses()
            case '4':
                student.list_enrolled_students()
            case '5':
                continue_asking = False
            case '6':
                main()
if __name__ == "__main__":
    main()