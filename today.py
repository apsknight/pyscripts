import datetime, urllib2

date = str(datetime.date.today())

month = date[5:7]
date = date[8:]

url = 'http://numbersapi.com/%s/%s/date' % (month, date)

data = urllib2.urlopen(url).read()

print data
