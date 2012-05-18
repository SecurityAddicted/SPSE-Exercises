#!/usr/bin/python

age = 18
while age >= 18:
	age = int(raw_input("What is your age?"))
	if age < 18:
		continue
	print "Your age is >= 18"
else:
	print "Not allowed"
