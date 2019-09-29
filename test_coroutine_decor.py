
# define a coroutine decorator to call __next__ method on a coroutine object

def coroutine(func):
    def starter(*args, **kwargs):
        g = func(*args, **kwargs)
        g.__next__()  # or next(g)
        return g
    return starter