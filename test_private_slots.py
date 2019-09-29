

# a memory efficient way of defining private attributes is use '__slots__' instance attribute

class Rect:
    __slots__ = ('__width', '__length')

    def __init__(self, width=None, length=None):
        self.__width = width or 1
        self.__length = length or 1


    @property
    def area(self):
        return self.__width * self.__length


r1 = Rect(10, 20)
print(r1.area)   # only area is visible, width and length are private

# __slots__ has efficient memory usage when there are huge number of instances 
for r in [Rect(w, l) for w in range(3) for l in range(6, 9)]:
    print(r.area)

# but slots has inheritance 'shadowing' effects

class SpecialRect(Rect):

    @property
    def area(self):
        return self.__width * self.__length

s1 = SpecialRect()

try:
    print(s1.area)
except AttributeError as ae:
    print(f"error: {ae}")  # => 'Sqr' object has no attribute '_Sqr__width'

# Therefore, in subclass the __slots__ has to be explicitely defined for all private attributes
# Instances can only have the attributes listed in __slots__, unless include '__dict__' in __slots__, 
# but doing so may negate the memory savings.
# 
# If not dealing with millions of instances, __slots__ is not recommended, but if large volumn of instances
# is needed, and most likely addressing data objects, the 'numpy' lib should be used to manage such collections
# instead of home-made classes. 

class MyRect(Rect):

    # not only new attr '__owner' but also '__width' and '__length' are explicitly defined in __slots__
    __slots__ = ('__width', '__length', '__owner')

    @property
    def owner(self):
        return self.__owner or 'anonymous'

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

sr = MyRect(10, 20)  # constructor method inherited from super class !
print(sr.area)  # => 200, 'area' property inherited from super class !

sr.owner = 'Alice'
print(f"owner: {sr.owner}")


