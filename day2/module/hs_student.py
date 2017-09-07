class HighSchoolStudent(Student):
    school_name = "ZPHS"
    #pass
    #override and acces parent methods
    def get_name_capitalized(self):
        parent_value=super().get_name_capitalized()
        return  parent_value + " -HS"