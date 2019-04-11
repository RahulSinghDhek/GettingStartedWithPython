__author__ = 'rdhek'

import scrapy
class Demo(object):
    def __init__(self):
        print 'I am in constructor'

    def __del__(self):
        print "I am in destructor"

if __name__=='__main__':
    d1 = Demo()

    print d1
