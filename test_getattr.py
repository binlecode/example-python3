
# different from __getattribute__ method (which is always called before accessing an attribte), __getattr__ is
# only called for attributes not yet defined





# To achieve similar method_missing call-back support in ruby, the python __getattr__ can be implemented
# to return a callable. 
# 
# In Python, when execute o.f(x), it's a two-step operation: First, get the f attribute of o, then call it 
# with parameter x. If the first step fails because there is no attribute f, Python invokes the method __getattr__.

# Note that it is easy to use the __getattr__ method to handle either missing properties or functions, but
# not both at the same time.


class DemoMethodMissingCallback:

    # intercepts method missing call back, this essentially returns a callable when its name is not defined
    def __getattr__(self, name):
        def wpr(*args, **kwargs):
            print(f"a missing method {name} is called on object {self}")
            print(f"the args are {args}, and the kwargs are {kwargs}")
        return wpr
    
    def foo(self):
        print('foo is called')


dmmc = DemoMethodMissingCallback()

dmmc.foo_method('bar_arg', k1='v1', k2=123)



# Now this is an interesting case, when a method with matching name but mismatching signature (args in this case),
# the __getattr__ is not invoked, because it only checks the name 'foo', and doesn't care if 'foo' is callable or not.
#
# In Python, methods are attributes too. 
#
try:
    dmmc.foo('abc')
except TypeError as te:
    print(f"error calling foo('abc'): {te}")

# also the __getattr__ defined above doesn't properly handle missing attributes that are not callable
print(dmmc.non_attrbt)  # => <function DemoMethodMissingCallback.__getattr__.<locals>.wpr at 0x...>


