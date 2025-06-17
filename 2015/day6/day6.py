import re

def solve1():
    lights = set()
    #1000 by 1000 grid - need to keep track of lights.
    #on - add x y cords to set, :off removes all x y from set and :toggle switches x y status in set
    #track 1d array for on and multiply at end
    with open("2015/day6/input.txt") as file:
        for line in file:
            line.strip()
            cords = list(map(int,re.findall(r'\d+', line)))
            x1,y1,x2,y2 = cords
            #print(line)
            if "toggle" in line:
                for x in list(range((x1),(x2+1))):
                    for y in list(range((y1),(y2+1))):
                        if ((x,y)) in lights:
                            lights.remove((x,y))
                        else:
                            lights.add((x,y))
            elif "off" in line:
                for x in list(range((x1),(x2+1))):
                    for y in list(range((y1),(y2+1))):
                        lights.discard((x,y))
            elif "on" in line:
                for x in list(range((x1),(x2+1))):
                    for y in list(range((y1),(y2+1))):
                        lights.add((x,y))
        print(f'{len(lights)}: part 1')
# trouble with range, first input is inclusive, while the second input of range is NOT INCLUSIVE, so must +1
# trouble keeping track of lights, used a set for cords with x1 x2 y1 y2
# part 2 needs a 2d array to change value, cant be less than 0 and return sum of all values.

def solve2():
    #on +1
    #off -1
    #toggle +2
    light2D = ([[0 for x in range(0, 1001)] for y in range(0, 1001)])
    #2d array, [1000][1000] all with value 0
    with open("2015/day6/input.txt") as file:
        for line in file:
            line.strip()
            cords = list(map(int,re.findall(r'\d+', line)))
            #print(cords)
            #format is (x1,y1) --- (x2,y2)
            x1,y1,x2,y2 = cords
            #print(line)
            if "toggle" in line:
                for x in range((x1),(x2+1)):
                    for y in range((y1),(y2+1)):
                        value = light2D[x][y]
                        light2D[x][y] = value+2
            elif "off" in line:
                    for x in range((x1),(x2+1)):
                        for y in range((y1),(y2+1)):
                            if light2D[x][y] == 0:
                                continue
                            value = light2D[x][y]
                            light2D[x][y] = value-1
            elif "on" in line:
                for x in range((x1),(x2+1)):
                    for y in range((y1),(y2+1)):
                        value = light2D[x][y]
                        light2D[x][y] = value+1
    sum = 0
    for x in range(1,1001):
        for y in range(1,1001):
            sum = sum + light2D[x][y]
    print(f'{sum}: part 2')

solve1()
solve2()

