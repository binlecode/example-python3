
import random

# try/except

class MyException(Exception):
    def __init__(self, *args, **kwargs):
        # super(self, *args, **kwargs) # this will raise error as Exception is not new-style class
        Exception.__init__(self, *args, **kwargs)

try:
    print("Are you happy?")
    rndInt = random.randrange(3)
    if rndInt == 0:
        assert False, 'I am a little low'
    elif rndInt == 1:
        raise MyException('Something is wrong')
    else:
        raise Exception('just not good')
except AssertionError as ae:
    print(f"alert: {str(ae)}")
    print('=> ok, drink a cup of coffee...')
except MyException as myEx:
    print(f"alert: {str(myEx)}")
    print("=> come on cheer up!")
except Exception as ex:
    print(f"alert: {str(ex)}")
    print('=> no worries, you still got wifi')
else: # will run when there's no exception
    print(f"no alert raised!")
finally:
    print("===> we'll be fine")


