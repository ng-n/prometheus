# Iterative Fibonacci
# Input: whole non negative integer N

import sys

n = int(sys.argv[1])

a, b = 0, 1

for i in range(n):
    a, b = b, a + b

print(a)
