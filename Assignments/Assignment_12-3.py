# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter URL:  ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

# Defines function lookupURL 
# returns the URL in given position
def lookupURL(url, position):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    tag = tags[position-1]
    return str(tag.get('href', None))

idx = 0   
while idx <= count:
    print "Retrieving:", url
    url = lookupURL(url, position)
    idx = idx + 1    