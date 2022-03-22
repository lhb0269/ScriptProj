import random
# def Student_data(*student):
#     global All_student_data
#     All_student_data += student
#     return All_student_data
# def show_data():
#     print("="*50)
#     print("Student",' '*5,'KOR',' '*3,'ENG',' '*3,'MATH',' '*3,'AVG')
#     print('-'*50)
#     for student in All_student_data:
#         print(student.get('number'),'\t'*3,student.get('KOR'),'\t',student.get('ENG'),'\t',student.get('MATH'),'\t',round(student.get('AVG'),2))
#     print('-' * 50)
#     print("=" * 50)
# All_student_data =[]
# for s in range(20):
#     student={'number':s+1,'KOR':random.randint(0,100),'ENG':random.randint(0,100),'MATH':random.randint(0,100)}
#     student.setdefault('AVG',(student.get('KOR') + student.get('ENG') + student.get('MATH')) / 3)
#     Student_data(student)
# show_data()

def gernerate_scores():
    scores = [{'kore':1,'eng':2,'math':3}for i in range(20)]
    kor = [random.randint(0,100) for i in range(20)]
    kor_avg = sum(kor)/3
    eng = [random.randint(0,100) for i in range(20)]
    math = [random.randint(0,100) for i in range(20)]
    student_acg=[(kor[i]+eng[i]+math[i])/3 for i in range(20)]


    pass

def process_scores():
    pass

def print_scores():
    pass