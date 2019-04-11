__author__ = 'rdhek'

def decorator_window(func):
    def wrapper(*args , **kwargs):
        return "[{}]".format(func(args[0]))
    return wrapper

@decorator_window
def print_window(val):
    return val

print print_window('test')

emailid="ravi.goglobium@gmail.com"