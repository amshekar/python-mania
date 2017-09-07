students=[]
def get_student_name():
    student_name=[]
    for student in students:
        student_name=student["student_name"].title()
    return  student_name

def print_student_name():
    student_name=get_student_name()
    print(student_name)

def add_student(student_name,student_id=15):
    student={"student_name":student_name,"student_id":student_id}
    students.append(student)

def var_args(name,*args):
    print(name)
    print(args)

#add_student("Shekar Gadamoni",48)
student_list=get_student_name()
student_name=input("Enter student NAme:  ")
student_id=input("enter student iD: ")
add_student(student_name,student_id)
print_student_name()
# print_student_name()
# var_args("shekar Gadamoni","Hello","All the best for your learning",None,True,1)