

# since class is also callable, so it can serve as decorator as well

class MyDec:
    def __init__(self, func):
        print('MyDec: __init__ invoked, this message only shows at decorating time, for once')
        self.func = func

    def __call__(self, *args):
        print('MyDec: __call__ invoked')
        print("MyDec: before calling ", self.func.__name__)
        res = self.func(*args)
        print("MyDec: result: ", str(res))
        print("MyDec: after calling ", self.func.__name__)


@MyDec
def m_func(*args) -> str:  # with return type annotation
    print("calling m_func with args:", args)
    return 'm_func done'

print('m_func: decorated, not called yet')

m_func('my arg')    # MyDec.__call__ called for each m_func invocation
m_func('my arg 2')

# non-@ decoration mode

def m_f(*args) -> str:
    print('calling m_f with args:', args)
    return 'm_f done'

mdf = MyDec(m_f)
mdf('non-@', 'works')

# a class decorator with arguments

# Now the process of decoration calls the constructor and then immediately invokes __call__(), 
# which can only take a single argument (the function object) and must return the decorated callable 
# object that replaces the original function

class MyDecWithArgs:
    def __init__(self, *dec_args): # only called once during compilation (decoration) time
        print('MyDecWithArgs: __init__ invoked, this message only shows at decorating time, for once')
        self.dec_args = dec_args

    # for class decorator with arguments, constructor __init__ now collects decorator arguments
    # and, the target fuction, f, is loaded in __call__ method
    # therefore, the __call__ is only called once during compilation (decoration) time
    # and, the decorated function that you return from __call__ method is used for the actual calls

    def __call__(self, f):
        print('MyDecWithArgs: __call__ invoked, this message only shows at decorating time, for once')

        def wrapper(*args):
            print("MyDecWithArgs: before calling:", f.__name__)
            print('MyDecWithArgs: decorator args:', self.dec_args)
            res = f(*args)
            print("MyDecWithArgs: result: ", str(res))
            print("MyDecWithArgs: after calling:", f.__name__)

        return wrapper   # wrapper will be called every time when target function is called


@MyDecWithArgs('dec1', 'dec2')
def mdwa_func(a, b):
    print('mdwa_func args:', a, b)

print('mdwa_func decorated, not called yet')

mdwa_func(1, 2)
mdwa_func(3, 4)


