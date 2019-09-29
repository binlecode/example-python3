

# class functions are assumed by instance as methods, but not the way around

class MyStuff:

    def __init__(self, name):
        self.name = name

    # function definition with self as first argument, so instance can call it as its own method
    def description(self):
        print('my name is {}'.format(self.name))


ms = MyStuff('cool stuff')

# call this function as instance method
ms.description()

# this is equivalent to the one above, calling description() function on the class directly with instance argument
MyStuff.description(ms)


