# Generator functions simply return objects with methods that handle next operations run by for loops
# at each level, and don’t produce any results until iterated.
# In other words, generator provide memory efficient way of iteration, esp for long sequences, such as
# big datasets and large files.

# Since generator functions retain their local scope state while active, it minimizes memory space requirements,
# and divides the work into shorter time slices.


def scramble(seq):
    print('scramble generator called')
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]

# Calling a generator function creates a generator object. However, it does not start
# running the function until the first next() is called on it.
sc = scramble('generator') 
# Same as sc.__next__(), on first next() call, the function:
#  - prints 'scramble generator ...'
#  - returns seq[i:] + seq[:i] for the i from the first iteration
# In fact, generator function ONLY executes on next() call, yield produces a value, and suspends 
# the function until another next() call.
print(next(sc))   
print(next(sc))
print(next(sc))


# use list function to create a list from a geneator - implicit iteration on generator
print(list(scramble('success')))

# below is a 'static' generator as the input sequence is fixed
s = 'dream'
# note the parenthesis '()' around the expression to provide a generator, instead of squire brackets '[]' that
# results in a true list
sg = (s[i:] + s[:i] for i in range(len(s)))  # expression format of generator definition
print(list(sg))


# use a lambda to build a 'quasi-static' generator
l = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))  # assign expression to a lambda output
lg = l(s)   # now call l() on input s to make it a generator
print(type(lg))  # => <class 'generator'>
print(list(lg))

s2 = 'another dream'
lg2 = l(s2)  # another generator with same expression but different sequence input
print(list(lg2))


# generator function called recursively
def permute(seq):
    if not seq:                               # Shuffle any sequence: generator
        yield seq                             # Empty sequence
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]        # remove current node
            for x in permute(rest):          # permute the others
                yield seq[i:i+1] + x          # add back the removed 'current' node


print(list(permute('abc')))

# or use generator as iterator manually
pg = permute('efg')
n = next(pg)
while n:
    print(n)
    n = next(pg, None)  # use default 'None' to avoid end of iteration exception




