#!/usr/bin/env python

from moduledemo import Scientific, quickadd

print 'Quick Add a+b: %d' %quickadd(10, 20)

ins = Scientific(5, 6)

print '%d' %ins.power()
