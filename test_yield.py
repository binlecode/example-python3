
# the yield statement defines a generator function, calling that function creates a generator instance
# besides returnning a value, yield can receive a value as well
# a yield statement receiving a value defines a coroutine function

# a generator can be a routine at the same with yield used in both ways


# generoutine

def generoutine():
    item = yield
    print('received item:', item)
    print('returning item:', item)
    yield item

gr = generoutine()
next(gr)  # activates first yield, so that data can be sent to it
itm = gr.send('two yields')

# with a loop

def gr_loop():
    while True:
        item = yield
        print('echoing item:', item)
        try:
            yield item
        except GeneratorExit:   # => on .close() call
            print('generator closed')
            break

gl = gr_loop()
next(gl)  # activates the yield assignment statement (coroutine behavior)
r = gl.send('round one')
print('generator return:', r)
next(gl)  # advances to a new iteration after yield item return (generator behavior)
r = gl.send('round two')
print('generator return:', r)
gl.close() # raises GeneratorExit at the yield, if not caught, the generator exists quietly





