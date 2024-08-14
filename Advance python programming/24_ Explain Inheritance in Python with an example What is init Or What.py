# Explain Inheritance in Python with an example? What is init? Or What 
# Is A Constructor In Python


# inheritance is oop that allows a class to inherit attributes and ethod
#from another class this allows for code reuse and the certion of a
# hierarchical class strcture

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"hello,my name is {self.name} and i am {self.age} ears old")

class Student(Person):
    def __init__(self, name, age, id):
        super().__init__(name,age)
        self.id = id
    def hello(self):
        print(f"hello,my name is {self.name} and i my student id is {self.id} ")

student = Student(name="Harry",age=20, id='120')

print(student.name)
print(student.age)
print(student.id)
print(student.hello())



# __init__

# - this method is a special called a constructer  it is automatically
#  called when an instance of the class is created.it allows the class to
# initilize the object attributes

# Constrctuor
# is a special method that is automatically called when a new instance of
# aclass is created.
