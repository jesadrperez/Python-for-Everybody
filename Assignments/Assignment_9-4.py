name = raw_input("Enter file:")
if len(name) < 1: 
    name = "mbox-short.txt"
handle = open(name)

d = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    d[email] = d.get(email,0) + 1
    # print words[1]
# print d    

val = d.values()
val.sort()

for key in d.keys():
    if d[key] < val[-1]:
        continue 
    print key, d[key]