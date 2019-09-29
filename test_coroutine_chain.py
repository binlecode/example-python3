
# instead of generator chain that 'pulls' data by for loop (the next() call), coroutines 
# are stacked together as a chain to 'push' the data down the pipeline by send() call.

# for a simple source -> filter -> sink pipeline

from test_coroutine_decor import coroutine

def src(target):
    for i in range(10):
        print('source number:', i)
        target.send(i)

@coroutine
def filter_odd(target):
    while True:
        nbr = (yield)  # wait on send() to feed data
        if nbr % 2 == 0:
            print('\t => even number, passing along')
            target.send(nbr)
        else:
            print('\t => odd number, blocking')

@coroutine
def sink():
    while True:
        nbr = (yield)
        print('\t\t => got numbrer:', nbr)


src(filter_odd(sink()))

