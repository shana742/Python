#  What relationship is appropriate for Course and Faculty?

# -> in object-oriented desing the relatinship between 'course and 'faculty'can
#    be modeled of their intercation. The most appropriate relationships are
#    association and aggregatio.
#->



class Faculty:
    def __init__(self,name):
        self.name = name

class Course:
    def __init__(self,course_name):
        self.course_name = course_name
        self.faculty_members = []

    def add_faculty(self, faculty):
        self.faculty_members.append(faculty)

prof1 = Faculty("harry")
prof2 = Faculty("roy")

course = Course("jAVA")
course.add_faculty(prof1)
course.add_faculty(prof2)

for faculty in course.faculty_members:
    print(faculty.name)
        
