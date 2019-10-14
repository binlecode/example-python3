
# an object that supports iteration has instance method __iter__ that returns an iterator
# the iterator has __next__ instance method that returns an element for each iteration (the 
# call to the __next__ method)

class MyIterable:

    def __init__(self, data=[]):
        self.data = data
        self.idx = 0

    # __iter__ operator overriding to return a custom iterator
    def __iter__(self):
        return self  # returning self as interator

    # since self is the iterator, the iterator.__next__ method becomes instance method of MyIterable class
    # the contract of iteration passed the last element is raising StopIteration exception
    def __next__(self):
        if self.idx < len(self.data):
            elm = self.data[self.idx] 
            self.idx += 1
            return elm
        else:
            raise StopIteration

# The rewindable subclass provides an iterator reset instance method
class MyRewindableIterable(MyIterable):

    def reset_iter(self):
        self.idx = 0

if __name__ == '__main__':    
    mi = MyIterable([1, 3, 5, 7, 9])
    print([x * 10 for x in mi])
    
    # Since the __iter__ returns the instance itself, the second trial of looping the same instance 
    # returns nothing. 
    # see ``test_iterator.py`` for an example of a separate stateful iterator 
    print([x * 10 for x in mi]) # prints an empty list since the 'for' generator returns nothing

    # Python doesn't have native definition of 'resetting' iterator object in general. For MyIterable class, 
    # a new instance is needed to provide a new iterator instance.
    mc = MyIterable('this is a string')
    print([x.upper() for x in mc])

    # The Rewindable class instance can be looped again after iterator reset
    mri = MyRewindableIterable([2, 4, 6, 8, 10])
    print([x * -1 for x in mri])
    print([x * -1 for x in mri])  # prints empty list

    mri.reset_iter()
    print([x * -1 for x in mri])  # prints empty list






    