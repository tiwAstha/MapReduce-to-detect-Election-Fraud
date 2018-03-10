from operator import itemgetter
import sys

current1 = None
current2 = None
w1 = None
w2 = None
difference = 0.0
x = 0.0
y = 0.0
per = 0.0

for n in sys.stdin:
    n = n.strip()
    w1, w2, count = n.split('\t')
    try:
        count = float(count)
    except ValueError:
        continue
    if current1 == w1 and current2 == w2:
    	y=count
    difference = y-x
    per = float(difference) / x * 100
    if per > 50:
        print ('%s\t%s\t%f' % (w1, w2, per))
    else:
        if w1 and w2:
            x=count

    current1 = w1
    current2 = w2
