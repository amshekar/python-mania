students = []
class Student:
    school_name="UPS"
#constructor self is equal to this in other languages
    def __init__(self,name,student_id=332):
        self.name=name
        self.student_id=student_id
        students.append(self)

# constructor to get rid of returning student object memory reference when we print below will overide that and return custom one
    def __str__(self):
        return  "Student " +self.name
    def get_name_capitalized(self):
        return self.name.capitalize()
    def get_school_name(self):
        return self.school_name
    #creating instance and accessing
shekar=Student("gadamoni",48)

print(shekar)
print(shekar.get_school_name())
print(shekar.get_name_capitalized())
#class variable accessing without creating instance
print(Student.school_name)
print(students)
