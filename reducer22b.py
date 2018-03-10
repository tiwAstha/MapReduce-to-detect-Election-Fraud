from operator import itemgetter
import sys

word = None
sum=0
column=[0.0,0.0,0.0]
for n in sys.stdin:
    n = n.strip()
    word, party, count = n.split('\t')
    party = int(party)
    word = int(word)
    count = int(count)
    if party == 1:
	sum+=count
	column[0]=float(count)
    if party ==2:
	sum+=count
	column[1]=float(count)
    if party ==3:
	sum+=count
	column[2]=float(count)
	column[0]= column[0]/sum * 100
	column[1]= column[1]/sum * 100
	column[2]= column[2]/sum * 100
        print '%f\t%f\t%f\t%f' % (word, column[0], column[1], column[2])
	column = [0.0,0.0,0.0]
	sum = 0

