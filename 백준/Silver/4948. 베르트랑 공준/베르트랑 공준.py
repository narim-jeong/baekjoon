import sys
import math

def prime(x):
    if x==0 or x==1: return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0: return False
    return True

value=list(range(123456*2))
prime_num=[]
for i in value:
    if prime(i): prime_num.append(i)

while True:
    n=int(sys.stdin.readline())
    if n==0: exit()
    count=0
    for j in prime_num:
        if n<j and j<=2*n: count+=1
    print(count)