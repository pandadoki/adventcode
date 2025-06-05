import re
def solve1():
    x = 0
    y = 0
    z = 0
    map = []
    #(1,1) to (1000,1000) grid - need to keep track of lights.
    #:on - leaves already on lights, :off turns off all and :toggle switches all of them.
    with open("2015/day6/input.txt") as file:
        for line in file:
            line.strip()
            map.extend(re.findall(r'\d+', line))
            if "toggle" in line:
                z = z+1
                print("toggle")
            elif "off" in line:
                x = x+1
                print("off")
            else:
                y = y+1
                print("on")
        print(map)
        print(f"{x}: off | {y}: on | {z}: toggle")

solve1()
