M, N = map(int, input().split())
arr = [list(map(str, input())) for _ in range(M)]
ans=64
for m_temp in range(M-7):
    for n_temp in range(N-7):
        ans_temp1 = 0
        ans_temp2 = 0
        for i in range(m_temp, m_temp+8):
            for j in range(n_temp, n_temp+8):
                if (i+j)%2==0:
                    if arr[i][j]!='B': ans_temp1+=1
                    elif arr[i][j]!='W': ans_temp2+=1
                else:
                    if arr[i][j] != 'W': ans_temp1 += 1
                    elif arr[i][j] != 'B': ans_temp2 += 1
        ans=min(ans, ans_temp1, ans_temp2)
print(ans)