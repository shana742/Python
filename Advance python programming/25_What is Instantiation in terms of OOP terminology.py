# What is Instantiation in terms of OOP terminology?

# -> the procces of creating an instance of a class.
# -> when u instantiate a class, you create an individual object
#    with its own unique set of attribtes that are defined by the class.This
#    object is called an instance f the class.


class Dog:
    def __init__(self, name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        return f"{self.name} syas woof!"
my_dog = Dog("Rex","German Shepherd")
print(my_dog.name)
print(my_dog.bark())
