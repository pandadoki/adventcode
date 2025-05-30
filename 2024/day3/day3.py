with open('2024/day3/input.txt') as file:
    for line in file:
        multi =  ["mul" + line for line in line.strip().split("mul")]
        print(multi)
    for line in multi:
        bracket = [line + ")" for line in line.strip().split(")")]
        print((bracket))

