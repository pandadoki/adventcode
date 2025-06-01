#MD5 Hashes, hexidecimal - start with 5 zeros
#find lowest positive number that produces a hash 
#part 2 was find lowest number that starts with 6 zeros 
import hashlib
def solvepart1n2():
    c1=c2=c3=c4=c5=c6=0
    with open("2015/day4/input.txt") as file:
        for line in file:
            line = line.strip()
            for x in range(10000000):
                m = line 
                key = (m + str(x))
                keyenc = (key).encode()
                ke = hashlib.md5(keyenc).hexdigest()
                if ke[:1] == "0":
                    c1=c1+1
                if ke[:2] == "00":
                    c2=c2+1
                if ke[:3] == "000":
                    c3=c3+1
                if ke[:4] == "0000":
                    c4=c4+1
                if ke[:5] == "00000":
                    c5=c5+1
                if ke[:6] == "000000":
                    c6=c6+1
                    print(x)
                    break
            print(f"{c1} + {c2} + {c3} + {c4} + {c5} + {c6}")

solvepart1n2()

