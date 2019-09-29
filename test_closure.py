
X = 99                   # Global scope name: not used

# f1 is a higher-order function that provides a closure scope for nested function f2
def f1():
    X = 88               # Enclosing def local, shadows global variable X

    def f2():
        print(X)         # Reference made in nested def

    f2()


f1()  # => 88, not 99


def f1():  # search local scopes of all enclosing defs, from inner to outer
    x = 99

    def f2():
        y = 'in f2'

        def f3():
            print(y)        # found in f2's local scope
            print(x)        # Found in f1's local scope

        f3()

    f2()


f1()  # => 99


# now let's see the tricky difference between mutable vs immutable variables in closure
# with immutable types like numbers, strings, tuples, etc., nested function can read, but never update
# If you try to rebind it, as shown below, then you are implicitly creating a local variable
def f1():
    x = 99
    y = 999
    ls = []

    def f2():
        ls.append(99)  # ls from f1 scope is mutable so this is legal
        print(ls)

        # this will raise 'use variable before assigning error'
        # because x is number thus immutable, therefore python treats x as a new local variable 'x'
        try:
            x = x + 1 
        except Exception as ex:
            print(ex)
        finally:
            # at this point, x is already a local variable although the previous '+=' operation failed
            x = 100   # assignment on local variable x
            print(x)


    f2()
    print(x)  # the global variable x is not changed => 99
    print(ls)  # [99]


f1()


# to avoid this limitation, comes the 'nonlocal' declaration
def f1():
    x = 99

    def f2():
        nonlocal x
        x = x + 1
        print(x)  # nonlocal x value is changed to 100

    f2()
    print(x)  # the nonlocal variable x is 100


f1()