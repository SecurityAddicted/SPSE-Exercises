#!/usr/bin/python

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

newCalculation = Calculator(10, 20)

print 'a+b: %d' %newCalculation.add()
print 'a*b: %d' %newCalculation.mul()

newPower = Scientific(2, 3)

print 'a+b: %d' %newPower.add()
print 'a*b: %d' %newPower.mul()
print 'a^b: %d' %newPower.power()
