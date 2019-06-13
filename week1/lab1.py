#!/usr/bin/env python

# Take Nth day of year and print dayOfMonth, Month

def dayofyear(day):
	if (day < 31):
		print day, "January"
	elif (day < 59):
		print day - 31, "February"
	elif (day < 90):
		print day - 59, "March"
	elif (day < 120):
		print day - 90, "April"
	elif (day < 151):
		print day - 120, "May"
	elif (day < 181):
		print day - 151, "June"
	elif (day < 212):
		print day - 181, "July"
	elif (day < 243):
		print day - 212, "August"
	elif (day < 273):
		print day - 243, "September"
	elif (day < 304):
		print day - 273, "October"
	elif (day < 334):
		print day - 304, "November"
	elif (day < 365):
		print day - 334, "December"

dayofyear(27)
dayofyear(43)
dayofyear(64)
dayofyear(115)
dayofyear(136)
dayofyear(159)
dayofyear(183)
dayofyear(237)
dayofyear(250)
dayofyear(298)
dayofyear(311)
dayofyear(353)
