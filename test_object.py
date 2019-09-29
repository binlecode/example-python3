

class Foo:
    """This is class Foo!"""

    # this is a class (constant) variable
    SIZE_THRESHOLD = 6  # there's no 'const' or 'final' keyword in python for constant variable

    # Data attributes need not be declared; like local variables,
    # they spring into existence when they are first assigned to.
    def __init__(self, size: int = 10, color: str = 'red'):
        # these are instance variables
        self.size = size
        self.color = color

    def is_large(self) -> bool:
        """ Returns boolean true if object's size is large, false otherwise """
        if self._size() > Foo.SIZE_THRESHOLD:
            return True
        else:
            return False

    def is_red(self):
        """ Returns boolean true if object color is read, false otherwise """
        if self.__color() == 'red':
            return True
        else:
            return False

    # underscore prefix as naming convention for 'protected' functions or attributes
    def _size(self):
        return self.size

    # double-underscore prefix as naming convention for 'private' functions or attributes
    def __color(self):
        return self.color


foo = Foo()
print(dir(foo))
print(Foo.is_large.__doc__)
print("foo is large? " + str(foo.is_large()))
print(Foo.is_red.__doc__)
print("foo is red? {}".format(foo.is_red()))

print(foo.is_large.__self__)  # method's owning class object
print(foo.is_large.__func__)  # method object itself

# it is easy to see Python has 'open'-class design
foo.height = 100
print("foo's height: " + str(foo.height))


