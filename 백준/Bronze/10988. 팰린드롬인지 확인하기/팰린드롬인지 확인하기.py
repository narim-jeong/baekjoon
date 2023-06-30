word=input()
length=len(word)

for i in range(int(length/2)+1):
    if word[i]!=word[length-1-i]: 
        print(0)
        break
if (i==int(length/2)) | (i==int(length/2)+1): print(1)