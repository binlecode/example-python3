# A context manager is a Python object that provides extra contextual information to an action. 
# This extra information takes the form of running a callable upon initiating the context using 
# the with statement, as well as running a callable upon completing all the code inside the with 
# block.

# `with ... as` is pythonic way of `try ... finally` for resource management

# such as open() function
with open(__file__, 'r') as f:
    print(f.name, 'total content length:', sum([len(l) for l in f]))

# the contract (API) for an object to be context manager is a pair of instance methods
# __enter__ and __exit__
# - If an error is raised in __init__ or __enter__ then the code block is never executed 
#   and __exit__ is not called
# - Once the code block is entered, __exit__ is always called, even if an exception is 
#   raised in the code block.


# implement context manager as a class
class MyOpen:
    def __init__(self, file_path, mode='r'):
        self.file = open(file_path, mode)

    def __enter__(self):
        print('my file openned')
        return self.file

    # __exit__ has callback signature holding exception context (ctx) references
    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()
        print('my file closed')

        if ctx_type:
            print(f"__exit__ => encountered exception with type: {ctx_type}")

try:

    with MyOpen(__file__) as f:
        print('reading my file')
        # __exit__ always runs despite this exception being raised
        raise Exception('raise custom exception in context block').with_traceback(None)
except Exception as e:
    print(f"code block => exception raised: {e}")
finally:
    pass


# implement context manager as a function with `@contextmanager` decorator

from contextlib import contextmanager

@contextmanager
def my_open(file_path, mode='r'):
    print(f"context manager => openning my file: {file_path}")
    f = open(file_path, mode)
    try:
        yield f
    finally:
        print(f"context manager => closing my file: {f.name}")
        f.close()


with my_open(__file__) as f:
    print(f"code block => reading file {f.name}")



    


