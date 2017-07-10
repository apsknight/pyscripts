import urllib2
import json

url = 'https://talaikis.com/api/quotes/random/'

quotes = urllib2.urlopen(url)
data = json.load(quotes)

print 'Quote: ' + data['quote']
print 'Author: ' + data['author']
print 'Category: ' + data['cat']