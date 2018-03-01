import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

total = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
   # Look at the parts of a tag
   #print 'TAG:',tag
   #print 'URL:',tag.get('href', None)
   #print 'Contents:',tag.contents[0]
   #print 'Attrs:',tag.attrs

   total = total + int(tag.contents[0])

print "Count", len(tags)
print "Sum", total