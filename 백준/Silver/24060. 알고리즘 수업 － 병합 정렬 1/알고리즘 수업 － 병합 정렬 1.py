import sys

def merge_sort(A):
    if len(A)==1: return A
    mid = (len(A)+1) // 2
    left=merge_sort(A[:mid])
    right = merge_sort(A[mid:])

    temp=[]
    i=0
    j=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            temp.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            ans.append(right[j])
            j+=1
    while i<len(left):
        temp.append(left[i])
        ans.append(left[i])
        i += 1
    while j<len(right):
        temp.append(right[j])
        ans.append(right[j])
        j += 1

    return temp

N, K=map(int,sys.stdin.readline().split())
A=list(map(int, sys.stdin.readline().split()))
ans=[]
merge_sort(A)

if len(ans)>=K: print(ans[K-1])
else: print(-1)