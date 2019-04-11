__author__ = 'rdhek'
dc = {i: hex(i) for i in range(9,16)}
from pprint import  pprint as pp
pp(dc)

dc = {i: hex(i) for i in range(9,19) if i%2}
pp(dc)