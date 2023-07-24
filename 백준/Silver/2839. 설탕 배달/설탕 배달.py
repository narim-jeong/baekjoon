N=int(input())
ans=-1
for num5 in range(1001):
    for num3 in range(1667):
        if 5*num5+3*num3>N: break
        elif 5*num5+3*num3==N:
            if ans==-1: ans=num5+num3
            else: ans=min(ans,num5+num3)
print(ans)