

# nested for loop
print([x + y for x in range(3) for y in [n * 10 for n in range(4)]])

# dictionary generation from list comprehension, this is new in python 3.x
print({x: x + 10 for x in range(3)})  # note the '{..}' wrapper to indicate a dictionary