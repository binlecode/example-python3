# a decorator in Python is a callable Python object that is used to modify a function, method or class 
# definition.
# The original object, the one which is going to be modified, is passed to a decorator as an argument.
# The decorator then returns a modified object that is callable.

# A key feature of decorators is that they run right after the decorated function is compiled. When the 
# compiler passes over the function definition, the resulting function object is passed to the decorator
# code, to produce a function-like object that replaces for the original function object.
# 
# That is usually at import time (i.e., when a module is loaded by Python).


# a function decorator
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
# for the second call, the string 'decorating function ...' won't show again
my_func(789)


# a function decorator with more general arguments
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

# the non-@ way of decoration
foo2 = func_dec(foo)  # note that the argument foo is already decorated once!
foo2('bar', k1='v1')


# decorator can be nested (meta-wrapper) to support arguments
def func_dec_meta(*dec_args):    # func_dec_super(...arguments...) needs to return a decorator
    def func_dec(func):                # nested function decorator that returns a function wrapper
        def func_wr(*args, **kwargs):  # nested function wrapper
            print("before calling ", func.__name__)
            print("with decorator arguments: ", str(dec_args))
            res = func(dec_args, **kwargs)  # replaces position args with decorator parameters in function call
            print("result: ", str(res))
            print("after calling ", func.__name__)

        return func_wr
    return func_dec


@func_dec_meta([1, 2, 3])   # func_dec_super([1,2,3]) needs to return a decorator that wraps the bar function
def bar(x, **kwargs):
    print("running bar with x: ", str(x))
    print("        and kwargs: ", str(kwargs))


# note that all positional args are 'shadowed' by decorator's parameter
bar('abc', 2000, k1='v1')  # => x: ([1, 2, 3],)


# this is the non-@ format of decoration

def bar2(x, **kwargs):
    print("running bar2 with x: ", str(x))
    print("         and kwargs: ", kwargs)

bar_dec_super = func_dec_meta([1, 2, 3])  # returns a decorator

bar3 = bar_dec_super(bar2)  # returns a wrapped function as a new function
bar3('abc', 2000, tag='for bar3')
bar2 = bar_dec_super(bar2)  # returns a wrapped function replacing the original
bar2('abc', 2000, tag='for bar2')


