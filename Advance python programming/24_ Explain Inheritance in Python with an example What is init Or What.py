# Explain Inheritance in Python with an example? What is init? Or What 
# Is A Constructor In Python


# inheritance is oop that allows a class to inherit attributes and ethod
#from another class this allows for code reuse and the certion of a
# hierarchical class strcture


class Animal:
    def __init__(self,name):
        self.name = name
    def speack(self):
        pass

class Dog(Animal):
    def speck(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speck(self):
        return f"{self.name} says Moof!"

dog = Dog("buddy")
cat = Cat("Whisker")

print(dog.speck())
print(cat.speck())


# __init__

# - this method is a special called a constructer  it is automatically
#  called when an instance of the class is created.it allows the class to
# initilize the object attributes

# Constrctuor
# is a special method that is automatically called when a new instance of
# aclass is created.
