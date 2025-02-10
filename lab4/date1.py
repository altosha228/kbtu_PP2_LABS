import datetime as a

date = a.datetime.now()
fiveDaysPrior = a.datetime(date.year, date.month, date.day - 5)
print(fiveDaysPrior.strftime("%x"))




def printDates():
  today = a.datetime().now()
  print(a.datetime(today.year, today.month, today.day - 1))
  print(a.datetime(today.year, today.month, today.day))
  print(a.datetime(today.year, today.month, today.day + 1))

def dateWithoutMicrosecs():
  today = a.datetime.now()
  print(a.datetime(today.year, today.month, today.day, today.hour, today.minute, today.second))


dateWithoutMicrosecs()