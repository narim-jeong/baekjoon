import sys
n=int(sys.stdin.readline())
people=dict()
for _ in range(n):
    name, state = map(str, sys.stdin.readline().split())
    if state=='enter': people[name]=state
    else: del people[name]
people=sorted(people.keys(), reverse=True)
print(*people, sep='\n')