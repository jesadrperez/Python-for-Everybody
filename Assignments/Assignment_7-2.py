# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
#fh = open('mbox-short.txt')

count = 0.0
zumm = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): 
        continue
    else:
        idx = line.find('0')
        num = line[idx:]
        num = float(num)
        zumm = zumm + num
        count = count + 1
        
print "Average spam confidence:", zumm/count