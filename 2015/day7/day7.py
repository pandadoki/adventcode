# wire A signal 
#(0, 2^16 - 1)
# bin() to conver to binary representation, 
# figure out operators and how to
circuits = {} 
def updateCircuit(x):
    print(x[-1])
    if x[-1] in circuits.items():
        print(circuits.items[x[-1]])
        #need to update every instance of the circuit and check and change the value to the updated one.
    for value in circuits:
        print(value)

def solve1():
    circuits = {}
    with open('2015/day7/input.txt') as file:
        for line in file:
            parts = [part.strip() for part in line.split('->')]
            circuits[parts[-1]] = parts[0]
            circuits = dict(sorted(circuits.items()))
        #print(circuits.items())
        while circuits['a'] == 'lx':
            for x in circuits.items():
                updateCircuit(x)
                if "AND" in x[-1]:
                    #print(x)
                    circuits[x[0]] = x[-1]
                elif "OR" in x[-1]:
                    circuits[x[0]] = x[-1]
                elif "RSHIFT" in x[-1]:
                    circuits[x[0]] = x[-1]
                elif "LSHIFT" in x[-1]:
                    circuits[x[0]] = x[-1]
                elif "NOT" in x[-1]:
                    parts = [part.strip() for part in x[-1].split('NOT')]
                    print(parts)
                    circuits[x[0]] = int((65536-1) - parts[-1])
                else:
                    circuits[x[0]] = x[-1]
                    circuits['a'] = 'lsklhf'

solve1()

