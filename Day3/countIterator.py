__author__ = 'rdhek'

from itertools import count , cycle ,repeat , imap , ifilter

from time import sleep
"""
for i in count(10):
    print i
    sleep(.15)

for i in cycle([1,2,3]):
    print i
    sleep(.15)
 """
for i in repeat([1,2,3],2):
    print i
    sleep(.15)

im = imap(hex,range(9,17))
print im
for i in im :
    print i

ifill = ifilter(lambda n : n%3==0 , range(1,10))

for i in ifill:
    print i