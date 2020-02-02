
# read `test_decorator.py` and `test_decorator_class.py` first

# the decoration target is a class (instead of function)

class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.

    The decorated class can define one `__init__` function that
    takes only the `self` argument. Also, the decorated class cannot be
    inherited from. Other than that, there are no restrictions that apply
    to the decorated class.

    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.
    """

    def __init__(self, orig_init):
        self._orig_init = orig_init

    def __call__(self, *args, **kwargs):
        """
        throws exception when called, to prevent default class constructor
        """
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.
        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._orig_init()  # call the original init function
            return self._instance


    def __instancecheck__(self, instance):
        """delegate the instance check to the decorated class instance
        """
        return isinstance(instance, self._instance)


# A Singleton instance is the decorator of MySingleton class
# therefore the Singleton instance methods become available as MySingleton class methods

@Singleton
class MySingleton:

    def __init__(self):
        print("MySingleton instance created: ", self)


m1 = MySingleton.instance()
m2 = MySingleton.instance()
assert m1 is m2  # they should be the same instance

ms = MySingleton()  # this should raise error

