# What is used to check whether an object o is an instance of class A ?

# Check whether an object 0 is an instance of class A using the 'isinstance()'
# function.


class A:
    pass
class B(A):
    pass
o= B()

print(isinstance(o,A))
print(isinstance(o,B))
print(isinstance(o,str))
      
