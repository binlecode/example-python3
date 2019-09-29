
class FooIterable:

    def __init__(self, data=[]):
        self.data = data

    def __iter__(self):
        return SkipIterator(self.data)


class SkipIterator:

    # iterator object wrapps iterable object's data
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 1
            return item

if __name__ == '__main__':
    fi = FooIterable(range(20))
    print([x for x in fi])
    # with separate stateful iterator, multiple iterations can apply to same iterable object
    print([x * 10 for x in fi])

