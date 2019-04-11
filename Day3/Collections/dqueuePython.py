__author__ = 'rdhek'

from collections import deque

print deque(open('../passwd'),3)

for line in deque(open('../passwd'),3):
    print line,
