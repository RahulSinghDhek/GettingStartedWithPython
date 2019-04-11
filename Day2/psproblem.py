__author__ = 'rdhek'
l = [2,3,1,6,7]
#list comprehension

def binaryprint(value):
    return "<binary>{}</binary>".format(value)
op=[]
for i in l:
    op.append(i *i)
print op

op2 = [i **i for i in l]
print op2
op2 = [bin(i) for i in l]
print op2
op2=[binaryprint(i) for i in l]
print op2

