fname = raw_input("Enter file name: ")
if fname == '':
    fname = 'romeo.txt'
fh = open(fname)

lst = list()

for line in fh:
    line = line.rstrip()
    words = line.split()
    
    for word in words:
        if word in lst:
            continue
        else:
        	lst.append(word)
lst.sort()
print lst