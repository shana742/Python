# What is Instantiation in terms of OOP terminology?

# -> the procces of creating an instance of a class.
# -> when u instantiate a class, you create an individual object
#    with its own unique set of attribtes that are defined by the class.This
#    object is called an instance f the class.


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def hello(self):
        print(f"hello,my name is {self.name} and i am {self.age} ears old")
p1 = Person("Harry",20)
p1.hello()