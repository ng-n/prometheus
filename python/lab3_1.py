# Input: Three variables a, b, c. 
# Output: "triangle" if out of given parameters can be formed a triangle, otherwise "not triangle"

import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a == 0 or b == 0 or c == 0 or (a + b <= c) or (b + c <= a) or (b + c <= a):
    print("not triangle")
else:
    print("triangle")
