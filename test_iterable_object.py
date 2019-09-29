

class MyIterable:

    def __init__(self, data=[]):
        self.data = data
        self.idx = 0

    # __iter__ operator overriding to return a custom iterator
    def __iter__(self):
        return self  # returning self as interator

    # since self is iterator, the iterator.__next__ method becomes instance method
    def __next__(self):
        if self.idx < len(self.data):
            elm = self.data[self.idx] 
            self.idx += 1
            return elm
        else:
            raise StopIteration 

if __name__ == '__main__':    
    mi = MyIterable([1, 3, 5, 7, 9])
    print([x * 10 for x in mi])
    # since the iterator is the object itself, not a new stateful object with its own index state, 
    # second round of iteration returns nothing
    # see ``test_iterator.py`` for an example of a separate stateful iterator 
    print([x * 10 for x in mi])

    mc = MyIterable('this is a string')
    print([x.upper() for x in mc])


    