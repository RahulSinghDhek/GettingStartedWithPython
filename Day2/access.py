__author__ = 'rdhek'

class Demo(object):
    def __setattr__(self, key, value):
        if key in self.__dict__:
            temp = self.__dict__.pop(key)
            if type(temp) is not list:
                temp=[temp]
            self.__dict__[key]= temp
            self.__dict__[key].append(value)
        else:
            self.__dict__[key]= value


if __name__=='__main__':
    d = Demo()
    setattr(d,'company','qualcomm')
    setattr(d,'company','ibm')
    setattr(d,'company','cisco')
    setattr(d,'company','google')
    print d
    #delattr(d,'company')
    print d.__dict__