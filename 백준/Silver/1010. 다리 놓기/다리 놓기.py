import sys

t=int(sys.stdin.readline())

def factorial(n):
    ans=1
    for i in range(2, n+1):
        ans*=i
    return ans

for _ in range(t):
    n, m=map(int, sys.stdin.readline().split())
    comb=int(factorial(m)/(factorial(n)*factorial(m-n)))
    print(comb)