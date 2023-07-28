import sys
n, m = map(int,sys.stdin.readline().split())
arr_n={str(sys.stdin.readline()) for _ in range(n)}
ans=0
for i in range(m):
    if sys.stdin.readline() in arr_n: ans+=1
print(ans)