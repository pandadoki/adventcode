flist = []
with open('2024/day2/input.txt') as file:
    lines = file.readlines()
    for line in lines:
        flist.append(line.strip())

x=0
for i in range(len(flist)):
    flist.sort()
    print(flist)
    for n in int(flist[i]):
        int(flist[i][n])
        if flist[i][n] < flist[i][n]-3 or flist[i][n] > flist[i][n]+3:
            x = x+1
        else: 
            x-1

print(x)
