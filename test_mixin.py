

# In python, avoid multiple inheritance altogether. Diamond inheritance of parent object state and 
# constructor ordering are error prone.

# In most cases, the need of the convenience and encapsulation that comes with multiple inheritance 
# can be met by writing a mix-in.
# A mix-in is a class that only defines a set of additional methods that a class should provide. Mix-in 
# classes don’t define their own instance attributes nor require their __init__ constructor to be called.

# Writing mix-ins is easy in Python as it inspects the current state of any object regardless of its type. 
# Dynamic inspection enables writing generic functionality a single time, in a mix-in, that can be applied 
# to many other classes. Mix-ins is the best solution for modular reuse.


from datetime import datetime
import json

class ToDictMixin:

    # mixin offers class level method

    @classmethod  
    def dict_size(cls, dict):
        return len(dict or {})

    # mixin offers instance level method

    def to_dict(self):
        return self._traverse_dict()

    def _traverse_dict(self):
        raise NotImplementedError()

    def describe_dict(self):
        dct = self.to_dict()
        for key in dct:
            print(f"key = {key}, value = {dct[key]}")


class Foo(ToDictMixin):

    def __init__(self, data=None):
        self._dict = data or {}
    
    # override mixin's 'protected' method with class internal implmentation
    def _traverse_dict(self):
        return self._dict

hash = {'a': 'abc', 'val': 12345, 'time': datetime.now()}
print(f"hash size: {Foo.dict_size(hash)}")  # use mixin's class method

f = Foo(hash)
f.describe_dict()   # use mixin's instance method


class ToJsonMixin:

    @staticmethod
    def _json_error_lmb(obj):
        if isinstance(obj, datetime):
            return f"{obj.year} - {obj.month} - {obj.day}"
        return str(obj)


    def describe_json(self):
        print(json.dumps(self.to_dict(), default=lambda o: ToJsonMixin._json_error_lmb(o)))
    
# class Bar has Foo as formal parent class, and with two mixins
class Bar(Foo, ToDictMixin, ToJsonMixin):
    pass


b = Bar(hash)

b.describe_json()





