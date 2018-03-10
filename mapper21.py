import sys
import re

for n in sys.stdin:
    n = n.strip()
    w=re.split("\t|\n",n)
    print '%s\t%s' % (w[2], 1)




