word=input().upper()
unique=list(set(word))
num=[0 for i in range(26)]

for i in unique:
    num[ord(i)-65]=word.count(i)

if num.count(max(num)) > 1: print("?")
else: print(chr(num.index(max(num))+65))