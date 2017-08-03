import urllib2

number = raw_input('Enter Number: ')

url = 'http://numbersapi.com/%s' % (number)

data = urllib2.urlopen(url).read()

print data