def solve1():
    x = 0
    y = 0
    z = 0
    with open("2015/day6/input.txt") as file:
        for line in file:
            line.strip()
            if "toggle" in line:
                z = z+1
                
            elif "off" in line:
                x = x+1
                
            else:
                y = y+1
                #print("on")
        print(f"{x}: off | {y}: on | {z}: toggle")

solve1()
