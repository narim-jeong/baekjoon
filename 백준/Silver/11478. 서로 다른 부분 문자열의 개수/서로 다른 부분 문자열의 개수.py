import sys
sentence=str(sys.stdin.readline().strip())
part=set()
for i in range(len(sentence)):
    for j in range(i, len(sentence)):
        part.add(sentence[i:j+1])
print(len(part))