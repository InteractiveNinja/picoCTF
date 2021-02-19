import string


def getFlag(arr):
    s = string.ascii_letters.upper()
    val = ""
    for i in arr:
        if type(i) ==  str:
            val += i
        else:
            val += s[i-1]
    return val


print(getFlag([16,9,3,15,3,20,6,"{",20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,"}"]))  