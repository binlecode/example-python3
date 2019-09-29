
# In Python, there are only two types of attribute visibility for a class’s attributes: public and
# private.
# Python convention of private attribute is double-leading underscore '__', also known as 'name mangling',
# and python compiler prefix private attributes with one underscore and its beloning ClassName.
# 
# There's no langauge enforcement of access prevention other than this name prefix.
# 

class Label:

    def __init__(self, content):
        self.__cnt = content

    @property
    def content(self):
        return f"Content: {self.__cnt}"


lb = Label('Tennis')

print(lb.content)

# content property is read-only due to lack of setter
try:
    lb.content = 'Soccer'
except AttributeError:
    print('no setter for content attribute, it may be private')

# __cnt is not accessible since it is private
try:
    print(lb.__cnt)
except AttributeError as exp:
    print(exp)

# but this runs as there's no real access prevention other than a ClassName prefix
print(lb._Label__cnt)

# private attribute is just a python name prefixed of appending its ClassName and one underscore
# as shown in instance __dict__ storage
print(lb.__dict__)  # => {'_Label__cnt': 'Tennis'}








