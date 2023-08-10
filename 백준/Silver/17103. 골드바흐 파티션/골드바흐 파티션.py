import sys
import math
t=int(sys.stdin.readline())

prime=[False, False]+[True]*999999

for i in range(2, 1000001):
    if prime[i]:
        for j in range(i*2, 1000001, i):
            prime[j]=False

for _ in range(t):
    n=int(sys.stdin.readline())
    count=0
    for k in range(2, int(n/2)+1):
        if prime[k] and prime[n-k]: count+=1
    print(count)