import sys

n, m = map(int, sys.stdin.readline().split())
arr={}
for _ in range(n):
    word=sys.stdin.readline()
    if len(word)<=m: continue
    if arr.get(word): arr[word][0]+=1
    else: arr[word] = [1, len(word), word]

ans=sorted(arr.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2]))

for i in ans: print(i[0], end="")