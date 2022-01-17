A,B = map(int,input().split())

lim = 10**18

import math
gcd = math.gcd(A,B)

lcm = A*B//gcd

if lcm > lim:
    print('Large')
else:
    print(lcm)