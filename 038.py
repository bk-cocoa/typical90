A, B = map(int, input().split())

lim = 10**18

import math
gcd = math.gcd(A, B)

lcm = A*B//gcd

print('Large') if lcm > lim else print(lcm)