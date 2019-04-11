__author__ = 'rdhek'

l=range(1,6)
print {i : bin(i) for i in l}
print { bin(i) for i in l}
for item in { bin(i) for i in l}:
    print int(item,2)