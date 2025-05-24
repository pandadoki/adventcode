#2lw+2wh+2hl
#calculate surface area

def solvepart1():
    sum = 0
    with open('2015/day2/input.txt') as file:
        for line in file:
            line = line.strip().split("x")

            smallest = int(line[0])
            ndsmallest = int(line[1])
            #assume [0,1] are the smallest, check if [2] is smaller than [0, or 1] [4 5 1] AND THEN, if [2] is smaller than [0], we check if [0] is smaller than [1]
            if int(line[2]) < smallest:
                smallest = int(line[2])
                if int(line[0]) < int(line[1]):
                    ndsmallest = int(line[0])
            elif int(line[2]) < ndsmallest:
                ndsmallest = int(line[2])
            present = ndsmallest * smallest

            sum = sum + ((2 * int(line[0]) * int(line[1])) + (2 * int(line[1]) * int(line[2])) + (2 * int(line[2]) * int(line[0]))) + present
    return sum

def solvepart2():
    sum = 0
    with open('2015/day2/input.txt') as file:
        for line in file:
            line = line.strip().split("x")

            smallest = int(line[0])
            ndsmallest = int(line[1])
            #assume [0,1] are the smallest, check if [2] is smaller than [0, or 1] [4 5 1] AND THEN, if [2] is smaller than [0], we check if [0] is smaller than [1]
            if int(line[2]) < smallest:
                smallest = int(line[2])
                if int(line[0]) < int(line[1]):
                    ndsmallest = int(line[0])
            elif int(line[2]) < ndsmallest:
                ndsmallest = int(line[2])
            ribbon = (2 * ndsmallest) + (2 * smallest)

            sum = sum + (int(line[0]) * int(line[1]) * int(line[2])) + ribbon
    return sum

print(solvepart1())
print(solvepart2())
