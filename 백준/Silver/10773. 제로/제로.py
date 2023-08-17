import sys
k=int(sys.stdin.readline())
arr=[]
sum=0
for _ in range(k):
    num=int(sys.stdin.readline())
    if num==0: sum-=arr.pop()
    else:
        sum+=num
        arr.append(num)
print(sum)