import sys
import re
for n in sys.stdin:
    n = n.strip()
    w=re.split('\t|\n',n)
    print '%s\t%s\t%s' % (w[1]+'_06',w[2], 1)
