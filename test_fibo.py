# fibonacci series simple generator in 4 lines
# this shows the elegance of python multi-assignment

a, b = 0, 1  
while a < 100:
    print(a)
    a, b = b, a + b

# a more formal class defintion of fibo geneator

class Fibo:
    """iterator that yields numbers in the Fibonacci sequence"""

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        x = self.a
        if x > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.b + self.a
        return x

print('fibo numbers:')
for f in Fibo(100):
    print(f)

