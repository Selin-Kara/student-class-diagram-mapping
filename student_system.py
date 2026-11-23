class Course:
    def __init__(self, course_code, course_name, credit):
        self.course_code = course_code
        self.course_name = course_name
        self.credit = credit

    def display_course(self):
        print(f"Course: {self.course_code} - {self.course_name} ({self.credit} Credits)")


class Student:
    def __init__(self, student_id, name, department):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course.course_name}.")

    def show_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print("Enrolled Courses:")
        for c in self.courses:
            print(f"- {c.course_name}")


# Test / Example Usage
c1 = Course("AII003", "Software Engineering", 4)
c2 = Course("AII020", "System Analysis and Design", 3)

s1 = Student("20231976", "Selin Kara", "Information Systems and Technology")
s1.add_course(c1)
s1.add_course(c2)

print("--------------------")
s1.show_info()
