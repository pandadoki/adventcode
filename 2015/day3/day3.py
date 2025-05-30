def solvepart1():
    track = set()
    count = (0,0)
    xcord = 0
    ycord = 0
    track = list(track)
    track.append(count)
    with open('2015/day3/input.txt') as file:
        for line in file:
            for char in line:
                if char == '^': 
                    ycord = ycord + 1
                    count = (xcord,ycord)
                    track.append(count)
                elif char =='<':
                    xcord = xcord - 1
                    count = (xcord,ycord)
                    track.append(count)
                elif char == 'v':
                    ycord = ycord - 1
                    count = (xcord,ycord)
                    track.append(count)
                elif char == '>':
                    xcord = xcord + 1
                    count = (xcord,ycord)
                    track.append(count)
        track = set(track)
        #print(track)
        answer = (len(track))
        print(f"Part 1: {answer}")
   
def solvepart2():
    track = set()
    track1 = set()
    track2 = set()
    count = (0,0)
    x1cord = 0
    y1cord = 0
    x2cord = 0
    y2cord = 0
    track1 = list(track1)
    track1.append(count)
    track2 = list(track2)
    track2.append(count)
    with open('2015/day3/input.txt') as file:
        for line in file:
            for index, char in enumerate(line):
                if (index % 2 == 0):
                    if char == '^': 
                        y1cord = y1cord + 1
                        count = (x1cord,y1cord)
                        track1.append(count)
                    elif char =='<':
                        x1cord = x1cord - 1
                        count = (x1cord,y1cord)
                        track1.append(count)
                    elif char == 'v':
                        y1cord = y1cord - 1
                        count = (x1cord,y1cord)
                        track1.append(count)
                    elif char == '>':
                        x1cord = x1cord + 1
                        count = (x1cord,y1cord)
                        track1.append(count)
                else:
                    if char == '^': 
                        y2cord = y2cord + 1
                        count = (x2cord,y2cord)
                        track2.append(count)
                    elif char =='<':
                        x2cord = x2cord - 1
                        count = (x2cord,y2cord)
                        track2.append(count)
                    elif char == 'v':
                        y2cord = y2cord - 1
                        count = (x2cord,y2cord)
                        track2.append(count)
                    elif char == '>':
                        x2cord = x2cord + 1
                        count = (x2cord,y2cord)
                        track2.append(count)
        allhouse = list(track1 + track2)
        allhouse = set(allhouse)
        #print(allhouse)
        answer = (len(allhouse))
        print(f"Part 2: {answer}")

solvepart1()
solvepart2()

#Completed
