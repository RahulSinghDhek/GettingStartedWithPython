__author__ = 'rdhek'

class Properties(object):
    def __init__(self):
        self.container={}
    def __setitem__(self, key, value):
        self.container[key]=value

    def __getitem__(self, key):
        return self.container.get(key)

    def __iter__(self):
        return iter(self.container)

if __name__=='__main__':
    p = Properties()
    p['hostname']= 'wsl'
    p['ipadd'] = '0.0.0.0'
    print p['hostname']
    print p['l']

    for name in p:
        print "{} -> {}".format(name,p[name])
