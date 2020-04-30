# Palindrome 
# Input: string (spaces, latin letters  and any numbers are ok)
# Output: "YES" if the input string is palindrome, otherwise "NO"

import sys, string

s = str(sys.argv[1].lower())
i = 0
j = len(s)-1
f = 1
while( i < j):
    while((s[i].lower()).isalnum() == False): i = i + 1
    while((s[j].lower()).isalnum() == False): j = j - 1
    a, b = s[i].lower(), s[j].lower()
    if a.isalnum() and b.isalnum:
        if( a != b ):
            f = 0

    i = i + 1
    j = j - 1

if(f == 0):
    print('NO')
else:
    print('YES')
