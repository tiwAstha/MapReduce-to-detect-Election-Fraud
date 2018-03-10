from operator import itemgetter
import sys

thisCount = 0
w1 = None
w2 = None
thisWord1 = None
thisWord2 = None

for n in sys.stdin:
    n = n.strip()
    w1, w2, count = n.split('\t')
    try:
        count = int(count)
    except ValueError:
        continue
    if thisWord1 == w1 and thisWord2 == w2:
        thisCount=thisCount+count
    else:
        if thisWord1 and thisWord2:
            print '%s\t%s\t%s' % (thisWord1,thisWord2, thisCount)
        thisWord1 = w1
        thisWord1 = w2
        thisCount=count
if thisWord1 == w1 and thisWord2 == w2 :
    print '%s\t%s\t%s' % (thisWord1,thisWord2, thisCount)

