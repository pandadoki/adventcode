def solvepart1():
    count = 0
    with open ('2015/day1/input.txt') as file:
        for line in file:
            for char in line:
                    if char == '(':
                        count = count+1
                    elif char == ')':
                        count = count-1
    return count

def solvepart2():
    count = 0
    with open ('2015/day1/input.txt') as file:
        for line in file:
            for index, char in enumerate(line):
                if count == -1:
                    return index
                else:
                    if char == '(':
                        count = count+1
                    elif char == ')':
                        count = count-1
    return count

print(solvepart1())
print(solvepart2())

#passed part 1 part 2
#part 2 used enumerate for the index that count first goes -1
#completed
