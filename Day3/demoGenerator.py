__author__ = 'rdhek'
def demo():
    print "before yield 1"
    yield 10
    print "after yield 1"

    print "before yield 2"
    yield 20
    print "after yield 2"

    print "before yield 3"
    yield 30
    print "after yield 3"


d= demo()
print d.next()
print d.next()
print d.next()

for i in demo():
    print i