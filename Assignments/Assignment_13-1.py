#$ python solution.py 
#Enter location: http://python-data.dr-chuck.net/comments_42.xml
#Retrieving http://python-data.dr-chuck.net/comments_42.xml
#Retrieved 4204 characters
#Count: 50
#Sum: 2...

import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter Location: ')
uh = urllib.urlopen(url)
data = uh.read()
print 'Retriving', url

tree = ET.fromstring(data)
lst = tree.findall('.//count')

print 'Count:', len(lst)

total = 0
for count in lst:
    total = total + int(count.text)
print 'Sum:', total