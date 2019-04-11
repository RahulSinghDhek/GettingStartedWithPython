__author__ = 'rdhek'

op = (i for i in range(1,10))
op1 =(i for i in xrange(1,50000))
op2 =[i for i in xrange(1,5000)]
print op
print op1.__sizeof__()
print op2.__sizeof__()
print op1.next()