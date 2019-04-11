__author__ = 'rdhek'

class Borg(object):
    _state ={}

    def __init__(self):
        self.__dict__=self._state

if __name__=='__main__':
    b = Borg()
    c = Borg()

    print id(b.__dict__)
    print id(c.__dict__)
