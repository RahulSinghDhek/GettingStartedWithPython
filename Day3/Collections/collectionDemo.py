__author__='rdhek'

from collections import Counter,OrderedDict

c = Counter('this is a simple content')
print c
for k in c:
    print "[{} : {}]".format(k,c.get(k))


d = OrderedDict()
d['name']='dell'
d['version']=2.3
d['shell']= 'bash'

print d