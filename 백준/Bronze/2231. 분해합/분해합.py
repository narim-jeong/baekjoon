n=int(input())

for i in range(n):
    temp=sum(map(int,str(i)))
    if (temp+i)==n: 
        print(i)
        exit()
print("0")