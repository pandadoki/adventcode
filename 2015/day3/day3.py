def solvepart1():
    track = tuple()
    count = 0

    with open('2015/day3/input.txt') as file:
        for line in file:
            for index, char in enumerate(line):
                track = list(track)
                if char == '^': 
                    count = [0,1]
                    track.append(count)
                elif char =='<':
                    count = [-1,0]
                    track.append(count)
                elif char == 'v':
                    count = [0,-1]
                    track.append(count)
                elif char == '>':
                    count == [1,0]
                    track.append(count)
                track = tuple(track)
        print(track)
        count = 0
        xcord = 0
        ycord = 0
        for index in track:
            for x,i in enumerate(index):
                print(track[i])
                ar = track[i]
                for m, i in enumerate(ar):
                    print('this is m: ' + str(m))
                    print(" this is i: " + str(i))
                    if m == 0:
                        xcord = xcord + i
                        print(xcord)
                    elif m == 1:
                        ycord = ycord + i
                        print(ycord)
                    count = count + 1
            print('final x cord ' + str(xcord))
            print('final y cord ' + str(ycord))

solvepart1()
