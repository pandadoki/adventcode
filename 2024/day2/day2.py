def solvepart1():
    count = 0
    with open('2024/day2/input.txt') as file:
        for line in file:
            store = 0
            safe = True
            line = line.strip().split()
            print(line)
            if (int(line[0]) - int(line[1]) > 0):
                print("decreasing")
                for x in line[1:]:
                    x = int(x)
                    print(x)
                    print(line[store])
                    if not(int(line[store]) - x > 1 and int(line[store]) - x < 3):
                        print("unsafe")
                        safe = False
                        break
                    else:
                        store = store+1
                if safe:
                    print(line)
                    count = count+1
            elif (int(line[1]) - int(line[0]) > 0): 
                print("increasing")
                for c in line[1:]:
                    c = int(c)
                    print(c)
                    print(line[store])
                    if not(c - int(line[store]) > 1 and c - int(line[store]) < 3):
                        print("unsafe")
                        safe = False
                        break
                    else:
                        store = store+1
                if safe:
                    print(line)
                    count = count+1
            else:
                count = count+1 
                break
        print(f"safe: {count}")
                

solvepart1()
