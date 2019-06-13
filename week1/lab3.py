#!/usr/bin/env python

def magic(s):
	dict = {"a":1,"e":2,"i":3,"o":4,"u":5} 
	try:
		return dict[s]
	except: KeyError
	print "Not found"


magic("x")
magic("a")
