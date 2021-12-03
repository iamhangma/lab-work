# convert second into day
sec = int(input("Enter second:"))
day = sec/(60*60*24)
hour = sec/(60*60)
minutes = sec/(60)
print ("The following day is {}" . format(day))
print ("The following hour is {}" . format(hour))
print ("The following minutes is {}" . format(minutes))
