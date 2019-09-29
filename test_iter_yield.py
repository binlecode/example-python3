# Any function that contains a yield statement is turned into a generator function. When called, 
# it returns a new generator object with automatic retention of local scope and code position, 
# an automatically created __iter__ method that simply returns itself, and an automatically 
# created __next__ method (next in 2.X) that starts the function or resumes it where it last left off.
#

def gen(seq):
    for i in seq:
        yield i * 2

# this might be a bad example as range() itself is a generator, 
# this code is to just show explicitly the inner-working between generator and iterator 
gg = gen(range(5))
gi = gg.__iter__()
print(gi.__next__())
print(next(gi))    # same as calling .__next__() method

gsi = iter(gen('hello'))
print(next(gsi), next(gsi))  # hh, ee
print(list(gsi))  # list begins from the left offset: ['ll', 'll', 'oo']

# one use case of yield is in class instance __iter__ method as an 'in-line' generator

class DoubleIterable:

    def __init__(self, data=[]):
        self.data = data

    # instead of returning an iterator, a yield generator is defined as a shortcut to 
    # save explicit __next__ call on the (otherwise returned) iterator object
    def __iter__(self):
        for v in self.data:
            yield v * 2

# with __iter__ + yield generator, __next__ is automatically implied
for i in DoubleIterable('double'):
    print(i.upper())

# below is the explicit, equivalent logic for the same printing
itr = iter(DoubleIterable('double')) # calls __iter__, which returns a yield generator
item = next(itr)
try:
    while item:
        print(item.upper())
        item = next(itr)
except StopIteration:
    pass

# use object directly as an iterable
print(list(i * 10 for i in DoubleIterable([1, 2, 3])))    

# one important advantage of __iter__ + yield combination is that because there's no 
# explict return of iterator, thus no dependency on a offset state either, 
# as a result, this yield backed __iter__ can support multiple iterations
di = DoubleIterable(range(10))
iter1 = iter(di)
print(next(iter1), next(iter1))  # displaying first two elements

iter2 = iter(di)
print(next(iter2), next(iter2))  # displaying first two elements again

