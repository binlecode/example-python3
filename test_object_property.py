
# external ref link: https://www.python-course.eu/python3_properties.php

class P:

    def __init__(self, x):
        self.x = x  # instance attribute assignment

p = P(123)
print("p.x: " + str(p.x))  # no attribute getter

# In the following example, we just put the code line "self.x = x" in the __init__ method and 
# the property method x. And we wrote "two" methods with the same name with property/setter decorator.

class P2:

    def __init__(self, x):
        self.x = x  # this assignment is intercepted by 'x.setter' method below

    @property  # property decorator makes this method a getter. basically property = mutator methods
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        # you can put custom logic to intercept assignment to instance attribute
        if x < 1000:
            self.__x = x + 1000
        else:
            self.__x = x

p2 = P2(500)
print("p2.x: " + str(p2.x))   # => p2.x: 1500



