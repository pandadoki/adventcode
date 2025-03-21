flist = []
count = 0
with open('2024/day2/input.txt') as file:
    lines = file.readlines()
    for line in lines:
        store = 0
        print(line)
        afterline = (line.strip().split())
        store = int(afterline[0])
        for x in afterline[1:]:
            x = int(x)
            print(x)
            print(store)
            if not ((store)+3 <= x <= (store)-3):
                print("yippee")
                store = x
            else:
                count = count+1
                break
print(count)
            