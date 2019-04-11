__author__ = 'rdhek'
class RangeError(StandardError):
    def __str__(self):
        return "{} : {}".format(self.__class__.__name__,self.message)

def check4limit(radiation):
    if not 0.3 <= radiation <= 0.7:
        raise RangeError('radiation level far too high or low: {}'.format(radiation))

try:
    check4limit(0.8)
except RangeError,e:
    print e