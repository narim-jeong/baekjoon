import sys
n=int(sys.stdin.readline())
count=0

for _ in range(n):
    sent=sys.stdin.readline().rstrip()
    if sent=='ENTER': arr=dict()
    else:
        if sent not in arr:
            arr[sent]=1
            count+=1
print(count)