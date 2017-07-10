import urllib2
import json

api = 'https://api.github.com/users/'

# print 'Enter Username:'
username = raw_input('Enter Username: ')

url = api + username

json_data = urllib2.urlopen(url)
data = json.load(json_data)

print 'Name: ' + str(data['name'])
print 'ID: ' + str(data['id'])
print 'Profile Link: ' + str(data['html_url'])
print 'Company: ' + str(data['company'])
print 'Blog: ' + str(data['blog'])
print 'Location: ' + str(data['location'])
print 'Bio: ' + str(data['bio'])
print 'Public Repository: ' + str(data['public_repos'])
print 'Public Gists: ' + str(data['public_gists'])
print 'Followers: ' + str(data['followers'])
print 'Following: ' + str(data['following'])
print 'On Github from: ' + str(data['created_at'][:10])