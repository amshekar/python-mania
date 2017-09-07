students = []
class Student:
#constructor
    def __init__(self,name,student_id=332):

        student={"name":name,"student_id":student_id}
        students.append(student)

# constructor to get rid of returning student object memory reference when we print below will overide that and return custom one
    def __str__(self):
        return  "Studentcustom"
student=Student("Gadamoni",48)

print(student)
print(students)
