class Student:
    def __init__(self, name, math_score, english_score, science_score):
        self.name = name
        self.scores = [math_score, english_score, science_score]
        self.math_score = math_score
        self.english_score = english_score
        self.science_score = science_score
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()

    def calculate_average(self):
        total = sum(self.scores)
        return total / len(self.scores)

    def calculate_grade(self):
        if self.average >= 90:
            return 'A'
        elif 80 <= self.average < 90:
            return 'B'
        elif 70 <= self.average < 80:
            return 'C'
        elif 60 <= self.average < 70:
            return 'D'
        else:
            return 'F'

    def display_info(self):
        print("Student Name | MATH | ENGLISH | SCIENCE | AVERAGE | GRADE |\n")
        print(f"{self.name} | {self.math_score} | {self.english_score} | {self.science_score} | {self.average} | {self.grade}\n")


class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def display_students_info(self):
        print("\nThe Student Info is:\n")
        for student_name, student in self.students.items():
            student.display_info()


if __name__ == "__main__":
    student_manager = StudentManager()

    while True:
        student_name = input('ENTER THE STUDENT\'S NAME: ')
        math_score = float(input("Enter The Student's Math Score: "))
        english_score = float(input("Enter The Student's English Score: "))
        science_score = float(input("Enter The Student's Science Score: "))

        student = Student(student_name, math_score, english_score, science_score)
        student_manager.add_student(student)

        cont = input("Do you want to enter values for other students: (yes/no) ")
        if cont.lower() == 'yes':
            continue
        else:
            student_manager.display_students_info()
            break
