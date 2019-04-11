__author__ = 'rdhek'

a=[1,3,5,7]
b=[1,2,3,4,5]

x= set(a)
y= set(b)

print list(x.intersection(y))
print x.union(y)
print x-y