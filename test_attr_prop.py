
'''
attribute is internal state holding, property is external API
'''

# a literal (non pythonic) way of attribute getter/setter
class Person:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    ''' getter '''
    def getName(self):
        return self.firstName + ' ' + self.lastName

    ''' setter '''
    def setName(self, name):
        tokens = name.split(' ')
        if tokens:
            self.firstName = tokens[0]
        if len(tokens) > 1:
            self.lastName = tokens[1]
        else:
            self.lastName = None
    
    # define a 'name' with property built-in with getter and setter
    name = property(getName, setName, None, 'name property document')


p = Person('John', 'Smith')
print(p.name)  # calling getName method

p.name = 'Harry Potter' # calling setName method
assert p.__getattribute__('firstName') == 'Harry'
assert p.__getattribute__('lastName') == 'Potter'

p.name = 'Marry'
assert p.__getattribute__('lastName') == None

'''
use decorator instead of direct property method call
'''

class Box:

    def __init__(self, lnth, wdth, hght):
        self.l = lnth
        self.w = wdth
        self.h = hght
    
    @property
    def volume(self):    # implicitly defined getter for property 'volume'
        "volume property docs"
        return self.l * self.w * self.h

    @property
    def height(self):
        "this is the height property of the box"
        return self.h
    
    @height.setter
    def height(self, hght):
        print(f"setting height to {hght}")
        self.h = hght

b = Box(1, 2, 3)
assert b.volume == 1 * 2 * 3

# this will raise AtrributeError as setter is not defined
try:
    b.volume = 12
except AttributeError as ae:
    assert str(ae) == "can't set attribute"

# since height property has a setter, let's change height value
b.height = 10
assert b.__getattribute__('h') == 10  # internal attribute 'h' is changed to 10
assert b.volume == 1 * 2 * 10

