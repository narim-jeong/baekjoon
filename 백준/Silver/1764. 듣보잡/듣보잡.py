import sys
n, m = map(int, sys.stdin.readline().split())
listen=dict()
listen_see=[]
for i in range(n):
    listen[sys.stdin.readline()]=1
for j in range(m):
    name = sys.stdin.readline()
    if name in listen: listen_see.append(name)
listen_see.sort()
print(len(listen_see))
print(*listen_see, sep='')