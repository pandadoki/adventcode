
def solvepart1():
    good = 0
    with open('2015/day5/input.txt') as file:
        for line in file:
            print(line)
            line.strip()
            vowel = 0
            double = 0
            for char in line:
                if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
                    vowel = vowel+1
            for index in range(1, len(line)-1):
                print(f"{line[index-1]} + {line[index]}")
                if line[index-1] == "a" and line[index] == "b": 
                    double = 0
                    break
                if line[index-1] == "c" and line[index] == "d": 
                    double = 0
                    break
                if line[index-1] == "p" and line[index] == "q":
                    double = 0
                    break
                if line[index-1] == "x" and line[index] == "y": 
                    double = 0
                    break
                if line[index-1] == line[index]:
                    double = double + 1
            print(f"{vowel} vowels")
            print(f"{double} double")
            if double >= 1:
                if vowel >= 3:
                    good = good+1
        print(good)    

#It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

def solvepart2():
    good = 0
    with open('2015/day5/input.txt') as file:
        for line in file:
            print(line)
            line.strip()
            pair = 0
            repeat = 0
            for index in range(1, len(line)-1):
                print(f"{line[index-1]} + {line[index+1]}")
                place = line[index-1] + line[index]
                print(place)
                print(line[index+1:])
                if place in line[index+1:]:
                    pair = pair + 1
                    print("this passes pair")
                if line[index-1] == line[index+1]: 
                    repeat = repeat + 1
                    print("this passes repeat")
            print(f"{repeat} repeat")
            print(f"{pair} pair")
            if repeat >= 2 and pair >= 1:
                good = good+1
        print(f"{good}: good strings")  


#solvepart1()
solvepart2()
