
import os

f = open('test_file.py', 'r')
for l in f:  # it is more memory efficient by iterating file lines instead of looping on f.readlines() return
    if len(l.strip()) <= 0:
        print("got an empty line")
    else:
        print("got line: " + l.rstrip())

if not f.closed:
    print('file is still open')

f.close()  # always apply close() statement to echo the 'open' statement

# with-as is based on context management protocol, supported types have two built-in
# methods: __enter__ and __exit__. 'with' calls __enter__, and __enter__ returns the object 
# assigned to 'as' following variable. 
# whether or not there is an exception, __exit__ is always called, similar to 'finally' block.
#
# this is the preferred way of openning file with resource auto-close even when there's an exception
with open('test_file.py', 'r') as f:
    num_lines = len(f.readlines())
    print('number of lines: {}'.format(num_lines))

# this is counting by streaming the file, which is more memory efficient
with open('test_file.py', 'r') as f:
    nl = 0
    for l in f:
        nl += 1
    print('number of lines {}'.format(nl))

# with-as can work with multiple context managers, such as file copy
with open('test_file.py', 'r') as fin, open('test_file_copy.py', 'w') as fout:
    for l in fin:
        fout.write(l)
# the above code is the same as
'''
fin = open('script2.py')
fout = open('upper.py', 'w')
try: # Same effect but explicit close on error
    for line in fin:
        fout.write(line.upper())
finally:
    fin.close()
    fout.close()
'''

# another resource auto-close way of counting lines for a file is using list comprehension
lnn = sum([1 for line in open('test_file.py', 'r') if line.strip()])
print("non-empty lines = ", lnn)

# use os open pipe to delegate to shell command
num_lines = os.popen('wc -l test_file.py', 'r')
print(num_lines.read())



