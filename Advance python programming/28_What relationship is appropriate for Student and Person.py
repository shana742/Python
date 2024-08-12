# What relationship is appropriate for Student and Person?
# -> object -oriented desing the relationship between 'student' and 'person' is typically
#    best reprsented by inheritance.


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"my name is {self.name} and iam {self.age} years old.")

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name}is studying")

student = Student("Harry",20,"S12345")

student.introduce()
student.study()
print(student.student_id)
