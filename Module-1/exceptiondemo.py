#!/usr/bin/python

class MyException(Exception):

        def __init__(self, value):
                self.value = value

        def __str__(self):
                return repr(self.value)

try:
        raise MyException('ommamma!')
except MyException as e:
        print 'MyException occured, value: ', e
