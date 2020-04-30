# Input data: Three variables x, y and z. x, y are non-negative numbers, z is equal to 0 or 1. x is not equal to 0. 
# Output data: The line "Everybody sing a song: <a song text>", where <a song text> is formed from 'y' couplets separated by spaces.
# If 'z' equals 1, an exclamation point is added at the end, otherwise a dot. 
# In the case of absence of couplets, no space / dot is added.
# Hint: apply row multiplications.

# Example:
# Input:    python3 lab2_2.py 2 3 1
# Output:   Everybody sing a song: la-la la-la la-la!

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

cuplet = (('-la'*x)[1:] + ' ')*y
sing = cuplet[0:len(cuplet)-1]

if y != 0 and z == 1:
    print('Everybody sing a song: ' + sing + '!')
elif y != 0 and z == 0:
    print('Everybody sing a song: ' + sing + '.')
elif y == 0 and z == 1:
    print('Everybody sing a song:' + sing + '!')
elif y == 0 and z == 0:
    print('Everybody sing a song:' + sing + '.')
