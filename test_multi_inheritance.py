
class GrandBase1:

    # private class variable
    __type = 'grand base 1'

    def greet(self):
        print("greet from " + self.__type)


class GrandBase2:
    __type = 'grand base 2'

    def greet(self):
        print("greet from " + self.__type)


class Base1(GrandBase1):

    __type = 'base 1'

    def hello(self):
        print("hello from " + self.__type)


class Base2(GrandBase2):

    __type = 'base 2'

    def hello(self):
        print("hello from " + self.__type)


class MyClass(Base1, Base2):

    __type = 'my class'

    def __init__(self, name: str):
        self.name = name




mc = MyClass('my new class')
# python does depth first method resolving, from SubBase1 to Base1, then to SubBase2 to Base2
mc.hello()  # => 'hello from base 1'
mc.greet()  # => 'greet from grand base 1'







