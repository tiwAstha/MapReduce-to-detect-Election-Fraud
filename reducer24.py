from operator import itemgetter
import sys

thisWord = None
thisCount = 0
word = None

for n in sys.stdin:
    n = n.strip()
    word, count = n.split('\t',1)
    try:
        count = int(count)
    except ValueError:
        continue
    if thisWord == word:
        thisCount = count+thisCount
    else:
        if wordCurrent :
            print '%s\t%s' % (thisWord, thisCount)
        thisCount = count
        thisWord = word

if thisWord== word :
    print '%s\t%s' % (thisWord, thisCount)
