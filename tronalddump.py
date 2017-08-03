import urllib, json, webbrowser

url = 'https://api.tronalddump.io/random/quote'

data = urllib.urlopen(url)

data = json.load(data)

print 'Pooped on: ' + data['appeared_at'][:10]
print '"' + data[value] + '"'

# webbrowser.open(data['url'])