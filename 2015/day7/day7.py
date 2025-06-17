# wire A signal 
#
#(0, 2^16)
# bin() to conver to binary representation, 
# figure out operators and how to 
d = 72
e = 507
f = 492
g = 114
h = 65412
i = 65079
x = 123
y = 456
def solve1():
    notCount = 0
    andCount = 0
    LshiftCount = 0
    RshiftCount = 0
    orCount = 0
    dCount = 0
    with open('2015/day7/input.txt') as file:
        for line in file:
            line = line.strip()
            if "AND" in line:
                andCount = andCount+1
                print("AND")
                print(line)
            elif "OR" in line:
                orCount = orCount+1
                print("OR")
                print(line)
            elif "RSHIFT" in line:
                RshiftCount = RshiftCount+1
                print("RSHIFT")
                print(line)
            elif "LSHIFT" in line:
                LshiftCount = LshiftCount+1
                print("LSHIFT")
                print(line)
            elif "NOT" in line:
                notCount = notCount+1
                print("NOT")
                print(line)
            else:
                dCount = dCount+1
                print("DECLARE")
                print(line)
    sum = LshiftCount+RshiftCount+orCount+andCount+notCount+dCount
    print(f'{LshiftCount} + {RshiftCount} + {orCount} + {andCount} + {notCount} + {dCount} + {sum}')

solve1()
