#!/usr/bin/env python

class Calculator(object):

        def __init__(self, inA, inB):
                self.a = inA
                self.b = inB

        def add(self):
                return self.a + self.b

        def mul(self):
                return self.a * self.b

class Scientific(Calculator):

        def add(self):
                return super(Scientific, self).add()

        def power(self):
                return pow(self.a, self.b)

def quickadd(a,b):
        return a+b
