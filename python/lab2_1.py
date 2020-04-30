# Solve equation f(x;m;q) = ( 1/(q*sqrt(2*Pi))  * exp(-(x-q)^2/2*q^2)

import sys
import math

x  = float(sys.argv[1])
u = float(sys.argv[2])
b = float(sys.argv[3])

print ( (1/(b * math.sqrt(2*math.pi))) * math.exp( -((x - u)*(x - u))/(2*b*b)) )
