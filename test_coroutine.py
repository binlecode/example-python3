
# Coroutines are similar to generators with a few differences. The main differences are:
# - generators are data producers
# - coroutines are data consumers

# A function that uses yield at the right side of the equation (as input) is a coroutine,
# which executes in response to values being sent to it.

# Coroutines only run in response to next() and send() calls.
# Coroutines must be "primed" by first calling next() (or send(None)), which advances execution 
# to the location of the first yield expression. At this point, it's ready to receive a value.

def echo():
    print('starting echo')
    msg = (yield)  # value passed to send() is returned by the (yield) expression
    print(f"echoing: {msg}")
    msg = (yield)
    print(f"echoing: {msg}")

ec = echo()
next(ec)
ec.send('coroutine rocks!')
try: 
    # will get StopIteration error since this send() will trigger another 'yield' but
    # there's no more yield statement, aka there's no yeild loop in this generator
    ec.send('python rocks!') 
except StopIteration as si:
    print('no more yield')

# typically yield is in a loop in a coroutine
def echo_loop():
    print('starting echo loop')
    while True:
        msg = (yield)
        print(f"echoing: {msg}")

el = echo_loop()
next(el)   # trigger coroutien to listen on 'yield' input

el.send('coroutine rocks')
el.send('yield rocks')
el.send('python rocks')

# A coroutine will typically run indefinitely unless it is explicitly shut down or it exits on
# its own. To close the stream of input values, use the close() method.
el.close()

# a self terminated coroutine by input
def echo_loop2():
    print('starting echo loop 2')
    while True:
        msg = (yield)
        print(f"echoing: {msg}")
        if msg == 'bye': 
            break

el2 = echo_loop2()
next(el2)
el2.send('coroutine rocks')
try:
    el2.send('bye')
except StopIteration:
    print('echo loop 2 stopped')


# it is clumsy to always need to explicity call __next__ method on a coroutine object
# this can be avoided by a function decorator

from test_coroutine_decor import coroutine

@coroutine
def receiver(subject):
    print(subject, 'is starting receiver')
    while True:
        msg = (yield)
        print(f"{subject} is receiving: {msg}")

rcvr = receiver('Snippet')
rcvr.send('coroutine next() is saved!')
rcvr.send('decorator works!')





        



