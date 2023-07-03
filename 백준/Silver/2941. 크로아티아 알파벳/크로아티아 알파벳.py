sentence=input()
num=0
for i in range(len(sentence)):
    if sentence[i]=='c':
        if i+1< len(sentence) and (sentence[i+1]=='-' or sentence[i+1]=='='): continue
    elif sentence[i]=='d':
        if i+1< len(sentence) and (sentence[i+1]=='-' or (i+2< len(sentence) and sentence[i+1]=='z' and sentence[i+2]=='=')): continue
    elif i+1< len(sentence) and sentence[i]=='l' and sentence[i+1]=='j': continue
    elif i + 1 < len(sentence) and sentence[i] == 'n' and sentence[i + 1] == 'j': continue
    elif i + 1 < len(sentence) and sentence[i] == 's' and sentence[i + 1] == '=': continue
    elif i + 1 < len(sentence) and sentence[i] == 'z' and sentence[i + 1] == '=': continue
    num=num+1
print(num)