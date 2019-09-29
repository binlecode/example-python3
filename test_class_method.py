

class Hello:

    host = 'master' # class attribute with initial value

    def __init__(self, host=None):
        self.host = host if host else Hello.host # pythonic ternary expression

    # to-string operator overloading
    def __str__(self):
        return f"this is host {self.host}"

    # instance method always with self (instance object) as first argument
    def greet(self, name):
        print(f"{self.host} says hello to {name}")

    # class method has no instance object, but class object, as first argument
    # therefore, class method can only change class state
    # one popular use of class method is factory method, where instances are created
    # with some (optional) class level states (aka class attributes)
    @classmethod
    def greet2(cls, name):
        print(f"{cls.host} says hello to {name}")

    # static method has no reference to instance or class object
    # therefore, static mthod can not change instance or class state
    # static methods are best for utility (state-less) functionalities
    @staticmethod
    def greet3(name):
        print(f"hello {name}")


hw = Hello('waitress')
print(hw) # calls hw.__str__()
hw.greet('guest')
# the above method call is interpreted by python as class method call with instance as first argument
Hello.greet(hw, 'another guest')

# calling class method
Hello.greet2('special guest')

# calling static method
Hello.greet3('utility method')

# use overloaded init method
hw2 = Hello()
hw2.greet('last guest')