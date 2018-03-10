from operator import itemgetter
import sys

thisCount = 0
thisWord = None
word = None

for n in sys.stdin:
    n = n.strip()
    word, count = n.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if thisWord == word:
        thisCount += count
    else:
        if thisWord:
            print '%s\t%s' % (thisWord, thisCount)
        thisCount = count
        thisWord = word
if thisWord == word:
    print '%s\t%s' % (thisWord, thisCount)

