import urllib2, json

base = raw_input('Base Currency? : ')
endpoint = 'http://api.fixer.io/latest?base=' + base.upper()

data = urllib2.urlopen(endpoint)

currency = json.load(data)

print 'BASE : ' + str(currency['base'])
print 'DATE : ' + str(currency['date'])
print '-----------------'

for key,value in currency['rates'].iteritems():
	print key + ': ' + str(value)