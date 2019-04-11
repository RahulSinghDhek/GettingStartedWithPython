__author__ = 'rdhek'

def yrange(stop=0,start=0):
    while start<stop:
        yield start
        start +=1

print yrange(10)
for i in yrange(5):
    print i