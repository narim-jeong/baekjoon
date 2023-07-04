grade=[list(map(str, input().split())) for _ in range(20)]

mult=0
tot_credit=0
for i in range(20):
    cred=float(grade[i][1])
    if grade[i][2]=='A+': grd=4.5
    elif grade[i][2]=='A0': grd=4.0
    elif grade[i][2] == 'B+': grd = 3.5
    elif grade[i][2] == 'B0': grd = 3.0
    elif grade[i][2] == 'C+': grd = 2.5
    elif grade[i][2] == 'C0': grd = 2.0
    elif grade[i][2] == 'D+': grd = 1.5
    elif grade[i][2] == 'D0': grd = 1.0
    else:
        grd=0.0
        if grade[i][2] == 'P': cred =0.0
    mult=mult+grd*cred
    tot_credit=tot_credit+cred

print(mult/tot_credit)