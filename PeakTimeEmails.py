name = raw_input("Enter File: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
document = handle.read()

timelist = list()
hoursdict = dict()
printlst = list()

document = document.splitlines()

for line in document:
    if line.startswith('From '):
        words = line.split()
        timelist.append(words[5])


for time in timelist:
    hms=time.split(':')
    hoursdict[hms[0]] = hoursdict.get(hms[0],0)+1



for h,c in hoursdict.items():
    printlst.append((h,c))
    
printlst.sort()

for h,c in printlst:
    print "Hour:{} | Count:{}".format(h, c)
