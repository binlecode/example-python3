

# to loop with index, use enumerate, which provides an indexed iterator

for idx, elm in enumerate(range(20, 30)):
    print(f"{idx} -th element: {elm}")

# it is clear from below that a tuple is returned for each iteration: (idx, value)
itr = enumerate(range(40, 50))
print(next(itr))   # => 0, 40
print(next(itr))   # => 1, 41
