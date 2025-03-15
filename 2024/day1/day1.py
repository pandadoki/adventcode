flist = []
with open('2024/day1/input.txt') as file:
    lines = file.readlines()
    for line in lines:
        numbers = line.strip().split()
        for num in numbers:
            flist.append(int(num))
rightSort = []
leftSort = []

for x in range(len(flist)):
    if(x%2):
        rightSort.append(flist[x])
    else:
        leftSort.append(flist[x])

rightSort.sort()
leftSort.sort()

z=0
for i in range(len(leftSort)):
    z = z+(abs((leftSort[i] - rightSort[i])))
print(z)
