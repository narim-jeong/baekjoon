import sys

n, k=map(int, sys.stdin.readline().split())

def factorial(n):
    ans=1
    for i in range(2, n+1):
        ans*=i
    return ans

comb=int(factorial(n)/(factorial(n-k)*factorial(k)))
print(comb)