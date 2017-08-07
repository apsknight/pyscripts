#! /usr/bin/python
                                                                                        
#    __ _ _ __ ___   __ _ _ __  _______  _ __  
#   / _` | '_ ` _ \ / _` | '_ \|_  / _ \| '_ \ 
#  | (_| | | | | | | (_| | | | |/ / (_) | | | |
#   \__,_|_| |_| |_|\__,_|_| |_/___\___/|_| |_|
#
# Python Script for scrapping product price from Amazon
# @Author: Aman Pratap Singh, www.amanpratapsingh.in
# @Date:   Aug 8, 2017
# @Email:  amanprtpsingh@gmail.com
# @Github username: @apsknight
# MIT License. You can find a copy of the License
# @http://aps.mit-license.org

import urllib2
from bs4 import BeautifulSoup
from tabulate import tabulate
from clint.textui import puts, indent, colored

banner = r"""

 	(  ___  )(       )(  ___  )( (    /|/ ___   )(  ___  )( (    /|
	| (   ) || () () || (   ) ||  \  ( |\/   )  || (   ) ||  \  ( |
	| (___) || || || || (___) ||   \ | |    /   )| |   | ||   \ | |
	|  ___  || |(_)| ||  ___  || (\ \) |   /   / | |   | || (\ \) |
	| (   ) || |   | || (   ) || | \   |  /   /  | |   | || | \   |
	| )   ( || )   ( || )   ( || )  \  | /   (_/\| (___) || )  \  |
	|/     \||/     \||/     \||/    )_)(_______/(_______)|/    )_)
                                                                
                              
                                 - By Aman Pratap Singh(@apsknight)
                                 
    """
puts(colored.yellow(banner))

request_headers = {
"Accept-Language": "en-US,en;q=0.5",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Referer": "http://thewebsite.com",
"Connection": "keep-alive" 
}

puts(colored.magenta("Amanzon Menu : "))
puts(colored.green("(1) Add Product Url."))
puts(colored.green("(2) Show Products price."))
index = int(raw_input("Action : "))
table = []

if index == 1:
	puts(colored.green("Enter URL: "))
	url = raw_input()
	fo = open('url.txt', 'a')
	fo.write('\n' + url)

elif index == 2:
	fo = open('url.txt', 'r')
	for url in fo:	
		req = urllib2.Request(url, headers = request_headers);
		page = urllib2.urlopen(req);
		soup = BeautifulSoup(page, 'html.parser')
		price = float(soup.find(id='priceblock_ourprice').text.strip().replace(',', ''))
		name = soup.find(id='productTitle').text.strip()
		table.append([name, price])
		# print url[0]
	fo.close()
	print tabulate(table, headers=['Item','INR'], tablefmt="fancy_grid")