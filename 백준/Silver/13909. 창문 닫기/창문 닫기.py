import sys
import math

n=int(sys.stdin.readline())
ans=0
x=1

while x*x<=n:
    ans+=1
    x+=1
print(ans)