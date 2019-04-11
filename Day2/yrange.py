__author__ = 'rdhek'

class yrangeiterator(object):
    def __init__(self,yro):
        self.yr = yro
    def next(self):
        temp = self.yr.start
        self.yr.start += 1

        if self.yr.start >self.yr.start:
            raise StopIteration()

        return temp

class yrange(object):
    def __init__(self,stop):
        self.stop = stop
        self.start = 0

    def __iter__(self):
        return yrangeiterator(self)


if __name__=='__main__':
    for i in yrange(5):
        print i
