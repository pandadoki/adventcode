def solvepart1():
    good = 0
    with open('2015/day5/input.txt') as file:
        for line in file:
            print(line)
            line.strip()
            vowel = 0
            double = 0
            for index in range(1, len(line)-1):
                print(f"{line[index-1]} + {line[index]}")
                if line[index-1] == "a" or line[index-1] == "e" or line[index-1] == "i" or line[index-1] == "o" or line[index-1] =="u":
                    vowel = vowel+1
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
            print(vowel)
            print(double)
            if double >= 1:
                if vowel >= 3:
                    good = good+1


 
        print(good)    

solvepart1()
