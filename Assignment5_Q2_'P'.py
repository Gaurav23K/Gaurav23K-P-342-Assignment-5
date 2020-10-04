'''
Assignment: 5
Q2: P(x) = x^4 - 3x^3 - 7x^2 + 27x - 18
'''

import math
import you_can

c = [1 , -3, -7, 27, -18]
def P(c, i, x):
    return ((c[0-i] * pow(x, 4))+(c[1-i] * pow(x, 3))+(c[2-i] * pow(x, 2))+(c[3-i] * pow(x, 1))+c[4-i])


a0 = 5
r = []
you_can.synthetic_Division(P, c, a0, r)

print("Roots of the Polynomial are : ")
for i in range(len(r)):
    print(r[i])
if(c[0]>0):
    print(-c[1])
else:
    print(c[1])

'''
********************************** OUTPUT *************************************
Roots of the Polynomial are : 
3.000031782399546
1.9999911672649806
0.9999633695467022
-2.999986319211229
'''