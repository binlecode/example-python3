# fibonacci series simple generator in 4 lines
# this shows the elegance of python multi-assignment

a, b = 0, 1  
while a < 100:
    print(a)
    a, b = b, a + b
