#! /usr/bin/python

'''
Python Script for scrapping product price from Amazon
'''
import urllib2, bs4
url = raw_input('URL? = ')

request_headers = {
"Accept-Language": "en-US,en;q=0.5",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Referer": "http://thewebsite.com",
"Connection": "keep-alive" 
}

req = urllib2.Request(url, headers = request_headers);
page = urllib2.urlopen(req);
soup = bs4.BeautifulSoup(page, 'html.parser')

price = float(soup.find(id='priceblock_ourprice').text.strip().replace(',', ''))

print price
