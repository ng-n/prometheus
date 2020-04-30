# Happy ticket
# A tiket called 'Happy' when the first three digits are equal to the sum of the last three.  
# Example: 030111 (0+3+0 = 1+1+1), 902326 (9+0+2=3+2+6), 001100(0+0+1 = 1+0+0)

# Input: two whole non-negative numbers (0 <= a1 <= a2 <= 999999)
# Output: Number of "Happy tickets" whose numbers are between a1 and a2. If the number is less than 6 digits, then zeroes are added to the beginning of the number


import sys

a1 = int(sys.argv[1])
a2 = int(sys.argv[2])

tot = 0
while a1 <= a2:
    a, sum1, sum2  = a1, 0, 0    
    for i in range (3):
        sum1 = sum1 + (a % 10)
        a = a // 10
    
    for i in range (3):
        sum2 = sum2 + (a % 10)
        a = a // 10
    
    if(sum1 == sum2): tot = tot + 1
    a1 = a1 + 1

print(tot)
