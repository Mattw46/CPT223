#!/usr/bin/env python

# Updated from Lab1, split function into two versions


# Accept number N and return day and month number
def getdayofyear(day):
	if (day < 31):
		return (day,1)
	elif (day < 59):
		return (day - 31,2)
	elif (day < 90):
		return (day - 59,3)
	elif (day < 120):
		return (day - 90,4)
	elif (day < 151):
		return (day - 120,5)
	elif (day < 181):
		return (day - 151,6)
	elif (day < 212):
		return (day - 181,7)
	elif (day < 243):
		return (day - 212,8)
	elif (day < 273):
		return (day - 243,9)
	elif (day < 304):
		return (day - 273,10)
	elif (day < 334):
		return (day - 304,11)
	elif (day < 365):
		return (day - 334,12)
	


# Accept day and month number and returns formatted string
def strday(day,month):
	if (month == 1):
		monthstring = "January"
	elif (month == 2):
		monthstring = "February"
	elif (month == 3):
		monthstring = "March"
	elif (month == 4):
		monthstring = "April"
	elif (month == 5):
		monthstring = "May"
	elif (month == 6):
		monthstring = "June"
	elif (month == 7):
		monthstring = "July"
	elif (month == 8):
		monthstring = "August"
	elif (month == 9):
		monthstring = "September"
	elif (month == 10):
		monthstring = "October"
	elif (month == 11):
		monthstring = "November"
	elif (month == 12):
		monthstring = "December"

	return str(day) + " " + monthstring


# test getdayofyear
print "27 is", getdayofyear(27)   # 27 January
print "43 is", getdayofyear(43)   # 12 February
print "64 is", getdayofyear(64)   # 5 March
print "115 is", getdayofyear(115) # 25 April
print "136 is", getdayofyear(136) # 16 May
print "159 is", getdayofyear(159) # 8 June
print "183 is", getdayofyear(183) # 2 July
print "237 is", getdayofyear(237) # 25 August
print "250 is", getdayofyear(250) # 7 September
print "298 is", getdayofyear(298) # 25 October
print "311 is", getdayofyear(311) # 7 November
print "353 is", getdayofyear(353) # 19 December

# test strday
print strday(27,1)
print strday(12,2)
print strday(5,3)
print strday(25,4)
print strday(16,5)
print strday(8,6)
print strday(2,7)
print strday(25,8)
print strday(7,9)
print strday(25,10)
print strday(7,11)
print strday(19,12)

