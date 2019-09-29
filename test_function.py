
#
# Ref: Learning Python 5th Ed, Table 18-1. Function argument-matching forms
#   Syntax                  Location    Interpretation
#   func(value)             Caller      Normal argument: matched by position
#   func(name=value)        Caller      Keyword argument: matched by name
#   func(*iterable)         Caller      Pass all objects in iterable as individual positional arguments
#   func(**dict)            Caller      Pass all key/value pairs in dict as individual keyword arguments
#   def func(name)          Function    Normal argument: matches any passed value by position or name
#   def func(name=value)    Function    Default argument value, if not passed in the call
#   def func(*name)         Function    Matches and collects remaining positional arguments in a tuple
#   def func(**name)        Function    Matches and collects remaining keyword arguments in a dictionary
#   def func(*other, name)  Function    Arguments that must be passed by keyword only in calls (3.X)
#   def func(*, name=value) Function    Arguments that must be passed by keyword only in calls (3.X)
#

# the example below shows difference between positional and keyword arguments
def func_1(name: str, color='red'):
    print("name: " + name + ", color: " + color)


func_1('apple')  # default second arg
func_1('ocean', color='blue')  # explicit keyword arg must follow positional arg, not the other way
func_1(name='cloud', color='white')  # can use positional arg the keyword way if it takes the lead
func_1('banana', 'yellow')  # implicit second arg by value


# the example below shows that the default arg is ONLY initialized once at function defining time
def func_2(hobby: str, hobbies=[]):
    hobbies.append(hobby)
    print(str(hobbies))


func_2('tennis')
# this will display two items, because the default arg is only initialized at function define time!
func_2('football')
# this resets the hobby list back to an empty list, and then adds the given hobby
func_2('golf', [])


# the example below shows variable arguments in different forms
# note the ordering: *args must occur before **keywords
def cheese_shop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    if kind in arguments:
        print("-- We are happy to serve you with", kind)
    else:
        print("-- I'm sorry, we're all out of", kind)

    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheese_shop('Holland')
cheese_shop('Holland', 'Blue Cheese', 'Goat Cheese', stock_size=100, stock_out_size=10)
cheese_shop('Holland', 'Holland', 'Blue Cheese', 'Goat Cheese', stock_size=100, client='John', clerk='Kurt')
