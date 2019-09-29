# a decorator in Python is a callable Python object that is used to modify a function, method or class 
# definition.
# The original object, the one which is going to be modified, is passed to a decorator as an argument.
# The decorator then returns a modified object.

# A key feature of decorators is that they run right after the decorated function is defined. That is 
# usually at import time (i.e., when a module is loaded by Python)

# use cases for decoraors
# * check arguments
# * collect runtime call trace info

# a function decorator must return a function
def func_decorator(func):
    print(f"decorating function {func}")
    def func_wrapper(x):
        print("before calling function: ", func.__name__)
        func(x)
        print("after calling function: ", func.__name__)

    return func_wrapper


@func_decorator
def my_func(x):
    print(f"running my_func({x})")
    print("x = " + str(x))


my_func(123)


# a more general defintion of a function decorator is to nest a function wrapper
def func_dec(func):
    def func_wr(*args, **kwargs):
        print("before calling ", func.__name__)
        res = func(*args, **kwargs)
        print("result: " + str(res))
        print("after calling ", func.__name__)

    return func_wr


@func_dec
def foo(*arg1, **dict1):
    print("running foo with args: ", str(arg1))
    print("  and with dict: ", str(dict1))


foo('bar', my_key='my-value')
foo('bar1', 'bar2', k1='v1', k2='v2')


# this is the non-@ version (programmatic format)
def foo2(*arg1, **dict1):
    print("running foo2 with args: ", str(arg1))
    print("         and with dict: ", str(dict1))


foo2 = func_dec(foo2)  # return a function to replace the original
foo2('bar', k1='v1')


# decorator can be nested (meta-wrapper) to support parameters
def func_dec_super(*dec_params):    # func_dec_super(...params...) needs to return a decorator
    def func_dec(func):                # nested function decorator that returns a function wrapper
        def func_wr(*args, **kwargs):  # nested function wrapper
            print("before calling ", func.__name__)
            print("feed args with wrapper args: ", str(dec_params))
            res = func(dec_params, **kwargs)  # replaces position args with decorator parameters in function call
            print("result: ", str(res))
            print("after calling ", func.__name__)

        return func_wr
    return func_dec


@func_dec_super([1, 2, 3])   # func_dec_super([1,2,3]) needs to return a decorator that wraps the bar function
def bar(x, **kwargs):
    print("running bar with x: ", str(x))
    print("        and kwargs: ", str(kwargs))


# note that all positional args are 'shadowed' by decorator's parameter
bar('abc', 2000, k1='v1')  # => x: ([1, 2, 3],)


# this is the non-@ format
def bar2(x, **kwargs):
    print("running bar2 with x: ", str(x))
    print("         and kwargs: ", kwargs)


bar_dec_super = func_dec_super([1, 2, 3])  # returns a decorator

bar3 = bar_dec_super(bar2)  # returns a wrapped function as a new function
bar3('abc', 2000, tag='for bar3')
bar2 = bar_dec_super(bar2)  # returns a wrapped function replacing the original
bar2('abc', 2000, tag='for bar2')


# since class is also callable, so it can serve as decorator as well
class MyDec:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print("before calling ", self.func.__name__)
        res = self.func(*args)
        print("result: ", str(res))
        print("after calling ", self.func.__name__)


@MyDec
def m_func(*args):
    print("calling m_func with args: ", args)

m_func('my arg')


# a better class decorator example for singleton pattern
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

    def __call__(self, *args, **kwargs):
        """
        throws exception when called, to prevent default class constructor
        """
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, instance):
        return isinstance(instance, self._instance)


@Singleton
class MySingleton:

    def __init__(self):
        print("MySingleton instance created: ", self)

try:
    ms = MySingleton()  # this should raise error
except TypeError:
    pass

ms = MySingleton.instance()
ms2 = MySingleton.instance()
assert ms is ms2  # they should be the same instance


# since decorators are functions thus they can be stacked

# d1 is a parameterized decorator
def d1(note='notified'):
    # to support argument in a decorator, a nested fuction is defined as the real decorator
    # this way d1 becomes the higher-order function that can receive 'metadata' by arguments
    def decor(func):  
        print('apply d1 decorate', note)
        return func
    return decor

def d2(func):
    print('apply d2 decorator')
    return func

@d1()  # have to add '()' to explicitly use default argument value
@d2
def func():
    print('running func')

func()   # => d1(note='notified')(d2(func))

@d2
@d1(note='be careful')
def func2():
    print('running func2')

func2()  # => d2(d1(note='be careful')(func2))

