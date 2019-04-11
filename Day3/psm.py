__author__ = 'rdhek'

name = ['pam','sam','tim','tom']

print map(str.upper,name)
print name
print ord("A")
ascii = map(ord,'aieou')
print ascii

#97
#'97[a]

print map(lambda value : "{}[{}]".format(value,chr(value)),ascii)

def tagit(value):
    return "{}[{}]".format(value,chr(value))
print map(tagit,ascii)
