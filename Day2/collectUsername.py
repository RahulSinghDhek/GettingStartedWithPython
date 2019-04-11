__author__ = 'rdhek'

userList=[]
with open('passwd') as fp:
    for line in fp:
        userList.append(line.split(':')[0])

from pprint import pprint as pp
#pp(userList)

ul=sorted([l.split(':')[0]for l in open('passwd') if l.startswith('a')])
#print ul

dict={}
dict={l.split(':')[0]:[l.split(':')[1:]] for l in open('passwd')}
#pp(dict)

dict1={l.split(':')[0]:l.rstrip().split(':')[1:] for l in open('passwd')}
pp(dict1)