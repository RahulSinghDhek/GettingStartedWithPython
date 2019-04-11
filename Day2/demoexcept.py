__author__ = 'rdhek'
from sys import  exc_info

def demo():
    try:
        1/1
    except:
        print exc_info()[1]

demo()