import sys
n, m = map(int, sys.stdin.readline().split())
poketmon=dict()
for i in range(n):
    name=str(sys.stdin.readline().strip())
    poketmon[name]=str(i+1)
poketmon_reverse=dict(map(reversed, poketmon.items()))
for _ in range(m):
    q=str(sys.stdin.readline().strip())
    if q.isdigit(): print(poketmon_reverse[q])
    else: print(poketmon[q])