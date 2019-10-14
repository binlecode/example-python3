

# nested for loop
print([x + y for x in range(3) for y in [n * 10 for n in range(4)]])

# dictionary generation from list comprehension, this is new in python 3.x
print({x: x + 10 for x in range(3)})  # note the '{..}' wrapper to indicate a dictionary

# use inline filter
print({x: x + 10 for x in range(10) if x % 2})  # only odd elements

# get (idx, elm) from each iterator using built-in enumerate
print({idx: x * 0-1 for idx, x in enumerate(range(10)) if not x % 2})  