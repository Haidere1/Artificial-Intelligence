def average_cal(scores):
    total=sum(scores)
    average=total/len(scores)
    return average

def grade_cal(average):
    if average >= 90:
        return 'A'
    elif 80<= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average <70:
        return 'D'
    else: 
        return 'F'

def display_info(data):
    print("Student Name | MATH | ENGLISH | SCIENCE | AVERAGE | GRADE |\n")
    print(data['name']," | ",data['math']," | ",data['englis']," | ",data['science']," | ",data['avg']," | ",data['grade'])
    print()

students={}

while True:
    student=input('ENTER THE STUDENTS NAME: ')
    
    
    math_score=float(input("Enter The Students Math Score: "))
    english_score=float(input("Enter The Students Math Score: "))
    science_score=float(input("Enter The Students Math Score: "))
   
    scores=[math_score,english_score,science_score]
    average=average_cal(scores)
    grade=grade_cal(average)

    students_dic={
        'name':student,
        'score':scores,
        'math':math_score,
        'englis':english_score,
        'science':science_score,
        'avg':average,
        'grade':grade
    }

    students[student]=students_dic

    cont=input("Do you want to enter values for other students: (yes/no) ")
    if cont.lower()== 'yes':
        continue
    else:
        print("\n The Student Info is:\n")
        for student, student_data in students.items():
            display_info(student_data)
    
        break


   
