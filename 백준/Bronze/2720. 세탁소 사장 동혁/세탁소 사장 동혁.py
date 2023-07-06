test_num=int(input())
money=[input() for _ in range(test_num)]

for i in range(test_num):
    charge=int(money[i])
    for j in [25, 10, 5, 1]:
        coin_num, charge = divmod(charge,j)
        print(coin_num, end=" ")
    print()