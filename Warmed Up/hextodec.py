import sys
def calc(string):
    hexs = ["0","1","2","3","4","5","6","7","8","9",'A','B','C','D','E','F']
    math = []
    dec = 0
    for i in range(len(string)):
        math.append([hexs.index(string[i]),(len(string)-1)-i])
    for m in math:
        dec += (m[0] * 16**m[1])
    return dec

if len(sys.argv) == 1:
    print("fuck off!")
else:
    print(calc(sys.argv[1]))

