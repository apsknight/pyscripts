import urllib2

number = raw_input('Enter Number: ')

url = 'http://numbersapi.com/%s/math' % (number)

data = urllib2.urlopen(url).read()

print data