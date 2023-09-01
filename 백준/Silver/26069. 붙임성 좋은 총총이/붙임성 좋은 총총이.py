import sys
n=int(sys.stdin.readline())
arr= {'ChongChong'}

for _ in range(n):
    sent=sys.stdin.readline().split()
    if sent[0] in arr:
        arr.add(sent[1])
    elif sent[1] in arr:
        arr.add(sent[0])
print(len(arr))