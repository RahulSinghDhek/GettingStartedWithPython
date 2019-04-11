__author__ = 'rdhek'
l = range(1,50)

print filter(lambda n: n%7 == 0,l)

def sumit(a,b):
    print "[{},{},{}]".format(a,b)
    return a +b
l = range(1,11)

print reduce(sumit,l)