__author__ = 'rdhek'
import re
def fileiter(files):
    for filename in files:
        yield open(filename)

def grep(regex , *filename):
    for fp in fileiter(filename):
        for lines in fp:
            if re.search(regex,lines,re.I):
                yield lines

for line in grep('root','passwd'):
    print line,
