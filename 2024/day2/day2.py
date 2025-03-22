flist = []
count = 0
with open('2024/day2/input.txt') as file:
    lines = file.readlines()
    for line in lines:
        store = 0
        print(line)
        afterline = (line.strip().split())
        store = int(afterline[0])
        print(int(afterline[1]))
        if (int(afterline[1]) - store < 0):
            print("decreasing")
            for x in afterline[1:]:
                x = int(x)
                print(x)
                print(store)
                if(x > store+3 and x - store < 0):
                    print("unsafe")
                    count = count+1
                    break
                else:
                    store = x
            else:
                count = count+1
                break
        elif (int(afterline[1]) - store > 0): 
            print("increasing")
            for c in afterline[1:]:
                c = int(c)
                print(c)
                print(store)
                if(c-3 > store and c - store > 0):
                    print("unsafe")
                    count = count+1
                    break
                else:
                    store = c
            else:
                count = count+1
                break
            
    print(f"safe: + {count}")
    print("")
print(count)
            