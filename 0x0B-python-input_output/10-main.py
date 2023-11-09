#!/usr/bin/python3
Student = __import__('10-student').Student

list_student_1 = Student("John", "Doe", 23)
list_student_2 = Student("Bob", "Dylan", 27)

j_student_1 = list_student_1.to_json()
j_student_2 = list_student_2.to_json(['first_name', 'age'])
j_student_3 = list_student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)
