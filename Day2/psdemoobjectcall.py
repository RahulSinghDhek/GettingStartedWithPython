__author__ = 'rdhek'

class Area(object):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def __call__(self, *args, **kwargs):
        return self.l * self.b

if __name__=='__main__':
    print Area(10,30)
