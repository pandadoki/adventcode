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
            print(line)
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
        print(len(lights))
# trouble with range, first input is inclusive, while the second input of range is NOT INCLUSIVE, so must +1
# trouble keeping track of lights, used a list for cords with x1 x2 y1 y2

def solve2():
    #on +1
    #off -1
    #toggle +2
    lights = set()
    with open("2015/day6/input.txt") as file:
        for line in file:
            line.strip()
            cords = list(map(int,re.findall(r'\d+', line)))
            x1,y1,x2,y2 = cords
            print(line)
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
        print(len(lights))

solve1()
solve2()

