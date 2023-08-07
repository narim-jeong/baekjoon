import sys
import math

num=int(sys.stdin.readline())

def prime(x):
    if x == 0 or x == 1: return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0: return False
    return True
    
for _ in range(num):
    n=int(sys.stdin.readline())
    j=n
    while True:
        if prime(j):
            print(j)
            break
        j+=1