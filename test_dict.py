# dict can be built from zip of two sequences

dc = dict(zip(range(5), reversed(range(5))))

print(dc)

dc = {"a": "value-a", 123: 456, "foo": None}

# will show None instead of the default value
print(dc.get("foo", "default value"))
# will show 'no such key' as default value for a non-existing key
print(dc.get(999, "no such key"))

# use pop() instead of get() will raise KeyError for a missing key
try:
    print(dc.pop(888))
except KeyError as ke:
    print('got exception:', type(ke), ke)


