import urllib

def read_text():
	quotes = open("/home/apsknight/hello.txt")
	content = quotes.read()
	print(content)
	quotes.close()
	check_profanity(content)

def check_profanity(content):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + content)
	output = connection.read()
	connection.close()

	if "true" in output:
		print("Profanity Alert!!")
	elif "false" in output:
		print("Good to go!!")
	else:
		print("Unable to open")

read_text()
