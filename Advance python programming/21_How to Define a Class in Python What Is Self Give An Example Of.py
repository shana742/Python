# How to Define a Class in Python? What Is Self? Give An Example Of 
# A Python Clas

# - class is bluprint for creating object
# - self parameter in method refers to the instance of the class .it
#   allows acces to the attribute and method of the class in oop

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"hello,my name is {self.name} and i am {self.age} ears old")
p1 = Person("Harry",20)
p1.hello()
