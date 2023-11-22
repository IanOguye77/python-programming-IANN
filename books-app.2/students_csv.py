students = open('students.txt', 'r')
all_students = students.readlines()
students.close()

# for student in all_students[1:]:
#     print(student.strip('\n'))

cleaned_student_data = []
for student in all_students[1:]:
    cleaned_student_data.append(student.strip('\n'))
    

# print(cleaned_student_data)
   
"Lewis is studying BBIT at JKUAT"
for student_data in cleaned_student_data:
    data = student_data.split(',')
    student_name = data[0].capitalize()
    university = data[1]
    degree = data[2]
    print(f"{student_name} is studying {degree} at {university}")

new_student = ",".join("joe,KU,Software Development".split(','))
# print(new_student)
with open('student.txt', 'a') as f:
    f.write(new_student + "\n")
    