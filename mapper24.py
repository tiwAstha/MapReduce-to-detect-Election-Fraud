import sys

for n in sys.stdin:
	n = n.strip()
	words = n.split()
			
	if words[2]=='1' and words[3]== '3':
		print '%s\t%s' % ('party 1-3',1)

	if words[2]=='3' and words[3]== '1':
		print '%s\t%s' % ('party 3-1',1)

	if words[2]=='3' and words[3]== '2':
		print '%s\t%s' % ('party 3-2',1)
	if words[2]=='1' and words[3]== '2':
		print '%s\t%s' % ('party 1-2',1)
	if words[2]=='2' and words[3]== '1':
		print '%s\t%s' % ('party 2-1',1)
	
	if words[2]=='2' and words[3]== '3':
		print '%s\t%s' % ('party 2-3',1)
