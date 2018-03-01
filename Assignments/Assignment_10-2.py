name = raw_input("Enter file:")
if len(name) < 1: 
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    timestamp = words[5].split(':')
    hour = timestamp[0]
    counts[hour] = counts.get(hour,0) + 1
    
lst = list()
for key, val in counts.items():
    lst.append((key, val))
    
lst.sort()

for key, val in lst:
    print key, val