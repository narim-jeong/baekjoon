n=int(input())
ans=0
for i in range(n):
    ans+=round((n-i-2)*(n-i-1)/2)
print("{0}\n{1}".format(ans,3))