class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def display_info(self):
        print("Student ID:", self.student_id)
        print("Student Name:", self.name)
        print("Student Age:", self.age)

    def display_course(self, course):
        print("Enrolled Course:", course.course_name)
        print("Course Code:", course.course_code)

    @classmethod
    def display_total_students(cls, student_list):
        print("Total Students:", len(student_list))
class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

    def display_course(self):
        print("Course Code:", self.course_code)
        print("Course Name:", self.course_name)


def add_student(student_list, student):
    student_list.append(student)
    print("Student added successfully!")

def display_students(student_list):
    for student in student_list:
        student.display_info()
        print("--------------------")
students = [
    Student("ST001", "Alice", 20),
    Student("ST002", "Student Two", 21),
    Student("ST003", "Student Three", 19)
]

course1 = Course("PROG211", "Object-Oriented Programming 1")

print("COURSE INFORMATION")
course1.display_course()

print("\nSTUDENT COURSE INFORMATION")
students[0].display_course(course1)


student_id = input("Enter Student ID: ").strip()
name = input("Enter Student Name: ").strip()

if not student_id or not name:
    print("Student ID and name cannot be empty.")

else:
    while True:
        try:
            age = int(input("Enter Student Age: "))

            if age <= 0:
                print("Age must be greater than zero.")
            else:
                break

        except ValueError:
            print("Please enter a valid whole number for age.")

    new_student = Student(student_id, name, age)
    add_student(students, new_student)

    print("\nALL STUDENT RECORDS")
    display_students(students)

    Student.display_total_students(students)    