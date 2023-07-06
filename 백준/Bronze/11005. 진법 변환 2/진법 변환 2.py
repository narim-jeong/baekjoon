num, digit=input().split()
digit=int(digit)
quot=int(num)
ans=[]
while quot!= 0:
    quot, rem = divmod(quot, digit)
    if rem>=10: ans.append(chr(rem+55))
    else: ans.append(rem)
for i in range(len(ans)): print(ans[len(ans)-1-i], end="")