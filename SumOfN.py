#sum of n numbers

import sys
s = 0
for i in sys.argv[1:]:
        s = s + int(i)
print(s)
