word_num=int(input())
word_list=[input() for _ in range(word_num)]
group_num=0

for i in range(word_num):
    no_group = 0
    for j in range(len(word_list[i])):
        if j+1<len(word_list[i]) and word_list[i][j]!=word_list[i][j+1]:
            for k in range(j+2, len(word_list[i])):
                if word_list[i][j]==word_list[i][k]: no_group=1
    if no_group == 0: group_num=group_num+1

print(group_num)