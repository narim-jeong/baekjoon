import sys
a, b = map(int, sys.stdin.readline().split())
A=dict()
B=dict()

arr=list(map(int, sys.stdin.readline().split()))
for i in range(a):
    A[arr[i]]=1
arr = list(map(int, sys.stdin.readline().split()))
for j in range(b):
    B[arr[j]]=1

count=0
for k in A:
    if k in B: count+=1
print(len(A)+len(B)-2*count)