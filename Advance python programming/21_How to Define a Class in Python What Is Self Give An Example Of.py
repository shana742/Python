# How to Define a Class in Python? What Is Self? Give An Example Of 
# A Python Clas

# - class is bluprint for creating object
# - self parameter in method refers to the instance of the class .it
#   allows acces to the attribute and method of the class in oop

class Dog:
    species = 'canis famili'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def description(self):
        return f"{self.name} is{self.age} yeras old"

    def bark(self, sound):
        return f"{self.name} says{sound}"

mydog = Dog('buddy',3)

print(mydog.species)
print(mydog.description())
print(mydog.bark('wolf'))
