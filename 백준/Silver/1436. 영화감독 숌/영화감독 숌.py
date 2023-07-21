n = int(input())
end_num=0
i=0
while True:
    i+=1
    temp=i
    while temp>=100:
        if temp%1000==666:
            end_num+=1
            break
        temp=temp//10
    if end_num==n:
        print(i)
        exit()