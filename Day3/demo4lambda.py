__author__ = 'rdhek'

"""
lambda arg1 , arg2 ,...  : expression
"""

print lambda n : n**2

sqr = lambda n : n**2
print sqr(5)

power = lambda x , n=0: x**n
print power(4,5)
print power(4)

raise_me = lambda n : n**2 if n>5 else n**3
print raise_me(3)