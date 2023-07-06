num, digit=input().split()
digit=int(digit)
tot=0
for i in range(len(num)):
    if num[i].isdecimal(): n=int(num[i])
    else: n=ord(num[i])-55
    tot+=(digit**(len(num)-i-1))*n
print(tot)