import json
import urllib

url = raw_input('Enter Location: ')
uh = urllib.urlopen(url)
data = uh.read()
print 'Retriving', url

info = json.loads(data)
print 'Retrieved :', len(info['comments'])

total = 0;
for item in info['comments']:
#    print 'Count', item['count']
#    print 'Name', item['name']
    total = total + item['count']
    
print "Sum:", total