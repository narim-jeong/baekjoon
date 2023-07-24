arr=[int(input()) for _ in range(5)]
arr.sort()
mean=sum(arr)//5
print('{0}\n{1}'.format(mean, arr[2]))