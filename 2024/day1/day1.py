def solvepart1():
    list_1 = []
    list_2 = []
    with open('2024/day1/input.txt') as file:
        for line in file:
            two_words = line.strip().split("   ")
            list_1.append(int(two_words[0]))
            list_2.append(int(two_words[1]))

    list_1.sort()
    list_2.sort()

    z=0
    for i in range(len(list_1)):
        z = z + (abs((list_1[i] - list_2[i])))
    print(z)

def solvepart2():
    list_1 = []
    list_2 = []
    with open('2024/day1/input.txt') as file:
        for line in file:
            two_words = line.strip().split("   ")
            list_1.append(int(two_words[0]))
            list_2.append(int(two_words[1]))
    list_1.sort()
    list_2.sort()
    z=0
    for i in range(len(list_1)):
        similarityScore = list_2.count(list_1[i])
        z = z + ((list_1[i] * similarityScore))
    print(z)


solvepart1()
solvepart2()
