
# Besides memory efficiency, another benefit of generator expressions is that they can be 
# composed together to form a stream processing pipeline.
# Essentially, a series of generators can be chained together into a pipe and pull items
# through it with a for-loop


gen1 = (x * 2 for x in range(100))

gen2 = (x + 1000 for x in gen1)  # gen2 pulls data from gen1

def gen3(gen):  # a generator function with explicit yield statement
    for x in gen:
        yield x * -1

# gen1 -> gen2 forms a stream pipeline with data lazy loading via next() call
print(next(gen2))
print(next(gen2))
print(next(gen2))

# stream continues with gen2 'pulled' by another generator gen3
print(next(gen3(gen2)))

# generators can be chained by `yield from` statement
# yield from transfers control to the 'from' generator

# gen4 has equivalent processing logic to gen3, but more decent
def gen4(gen):
    d = yield from gen
    return d * -1

print(next(gen4(gen2)))
